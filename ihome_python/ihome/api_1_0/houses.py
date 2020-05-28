from . import api1
from flask import g, current_app, request, jsonify, session
from ..utils.commons import login_required
from ..utils.image_storage import storage
from ..utils.response_code import RET
from ..models import User, Area, House, HouseImage, Facility, Order
from .. import constants, db, redis_store

import json
from sqlalchemy import and_, or_
import datetime



@api1.route('/areas')
def get_area_info():
    try:
        area_json = redis_store.get('areas_info')
    except Exception as e:
        current_app.logger.error(e)
    else:
        if area_json is not None:
            current_app.logger.info('hit redis areas_info')
            return area_json, 200, {'Content-Type': 'application/json'}

    try:
        areas = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='Get Areas DB err')

    area_dict_li = []
    for area in areas:
        area_dict_li.append(area.to_dict())

    area_dict = dict(errno=RET.OK, errmsg='sucess get area', data=area_dict_li)
    area_json = json.dumps(area_dict)

    # 'flask.wrappers.Response'
    # a = jsonify(errno=RET.OK, errmsg='sucess get area', data=area_dict_li)

    try:
        redis_store.setex('areas_info', constants.AREA_REDIS_EXPIRE_TIMES, area_json)
    except Exception as e:
        current_app.logger.error(e)


    return area_json, 200, {'Content-Type': 'application/json'}


@api1.route('/houses/info', methods=['POST'])
@login_required
def sava_house_info():
    """保存房屋的基本信息
        前端发送过来的json数据
        {
            "title":"",
            "price":"",
            "area_id":"1",
            "address":"",
            "room_count":"",
            "acreage":"",
            "unit":"",
            "capacity":"",
            "beds":"",
            "deposit":"",
            "min_days":"",
            "max_days":"",
            "facility":["7","8"]
        }
        """
    user_id = g.user_id
    house_data = request.get_json()
    if house_data is None:
        return jsonify(errno=RET.PARAMERR, errmsg='sava house info param err')


    title = house_data.get("title")  # 房屋名称标题
    price = house_data.get("price")  # 房屋单价
    area_id = house_data.get("area_id")  # 房屋所属城区的编号
    address = house_data.get("address")  # 房屋地址
    room_count = house_data.get("room_count")  # 房屋包含的房间数目
    acreage = house_data.get("acreage")  # 房屋面积
    unit = house_data.get("unit")  # 房屋布局（几室几厅)
    capacity = house_data.get("capacity")  # 房屋容纳人数
    beds = house_data.get("beds")  # 房屋卧床数目
    deposit = house_data.get("deposit")  # 押金
    min_days = house_data.get("min_days")  # 最小入住天数
    max_days = house_data.get("max_days")  # 最大

    #
    if not all([title, price, address, area_id, room_count, acreage, unit, capacity, beds, deposit, min_days, max_days]):
        return jsonify(errno=RET.PARAMERR, errmsg='house info incomplete')

    try:
        price = int(float(price) * 100)
        deposit = int(float(deposit) * 100)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='house info param err')

    try:
        area = Area.query.get(area_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='save house info area err')

    if area is None:
        return jsonify(errno=RET.NODATA, errmsg='sava house area not exists')

    house = House(
        user_id=user_id,
        area_id=area_id,
        title=title,
        price=price,
        address=address,
        room_count=room_count,
        acreage=acreage,
        unit=unit,
        capacity=capacity,
        beds=beds,
        deposit=deposit,
        min_days=min_days,
        max_days=max_days

    )

    # try:
    #     db.session.add()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.DBERR, errmsg='save base house info err')

    facility_ids = house_data.get('facility')
    print('facility_ids:', facility_ids)
    if facility_ids:
        # ["7","8"]
        try:
            facilities = Facility.query.filter(Facility.id.in_(facility_ids)).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='facility not in db')

        # 在house表中添加的facilities,是对象
        if facilities:
            print('facilities:', type(facilities), facilities)
            house.facilities = facilities

    try:
        db.session.add(house)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="保存数据失败")

    return jsonify(errno=RET.OK, errmsg="OK", data={"house_id": house.id})


@api1.route('/houses/image', methods=['POST'])
@login_required
def sava_house_image():
    image_file = request.files.get('house_image')
    house_id = request.form.get('house_id')
    print('image_file and house_id:', image_file, house_id)

    if not all([image_file, house_id]):
        return jsonify(errno=RET.PARAMERR, errmsg='house image param incomplete')

    # 检查用户是否注册
    try:
        house = House.query.filter_by(id=house_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='save image query house err')

    if house is None:
        return jsonify(errno=RET.NODATA, errmsg='house data not exists')


    # 将图片上传到七牛
    image_data = image_file.read()
    print('image_data:', type(image_data))

    try:
       file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg='qiniu save house image err')


    #将图片连接保存到数据库

    # 因为House表中的images字段，是relationship, 关系的
    # 对于多张图片保存可以使用这个字段
    # 现在只有一张图片，所以保存到HouseImage表中
    house_image = HouseImage(house_id=house_id, url=file_name)
    db.session.add(house_image)

    # HouseImage表中如果图片保存成功，先不提交，
    # 等House表中的index_image_url，字段成功添加后，一起提交

    if not house.index_image_url:
        house.index_image_url = file_name
        db.session.add(house)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='sava house and house-image err')

    image_url = constants.QINIU_URL_DOMAIN + file_name
    return jsonify(errno=RET.OK, errmsg='upload house image sucess', data={'image_url': image_url})


@api1.route('/houses/index')
def get_index_houses():

    # 查看redis当中有没有缓存数据
    try:
        home_houses_data = redis_store.get('home_houses_data')
        # print('home_houses_data:', type(home_houses_data), home_houses_data)
    except Exception as e:
        current_app.logger.error(e)
        home_houses_data = None

    if home_houses_data:
        current_app.logger.info('hit index houses data redis')
        # return 'data: {}'.format(houses_data_str), 200, {'Content-Type': 'application/json'}
        return '{"data": %s , "errno": %s , "errmsg": "OK"}' % (home_houses_data.decode(), RET.OK), 200, {'Content-Type': 'application/json'}

    # 取出满足条件的房源信息，放在index页面
    try:
        houses = House.query.filter(and_(or_(House.user_id == 6, House.user_id == 7)), ~(House.index_image_url == '')).all()
        # houses = House.query.order_by(House.order_count.desc()).limit(constants.HOME_PAGE_MAX_HOUSES)

        print('houses:', houses)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='get index houses err')

    if houses is None:
        return jsonify(errno=RET.NODATA, errmsg='get index houses err')

    houses_data = []
    for house in houses:
        # # 判断有没有index_image_url字段，也可以这么写
        # if not house.index_image_url:
        #     continue
        houses_data.append(house.to_basic_dict())

    houses_data_str = json.dumps(houses_data)

    # 将取出的信息放在redis中
    try:
        redis_store.setex('home_houses_data', constants.INDEX_HOUSES_EXPIRE_TIMES, houses_data_str)
    except Exception as e:
        current_app.logger.error(e)


    return '{"data": %s , "errno": %s , "errmsg": "OK"}' % (houses_data_str, RET.OK), 200, {'Content-Type': 'application/json'}
    # return jsonify(errno=RET.OK, errmsg='OK', data=houses_data)


@api1.route('/user/houses')
@login_required
def get_user_houses():
    user_id = g.user_id

    try:
        user = User.query.filter_by(id=user_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='get user houses db err')

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg='get user houses db no data')

    houses = user.houses
    # print('houses:', type(houses), houses)  # [<House 5>, <House 6>, <House 7>]
    houses_li = []
    for house in houses:
        houses_li.append(house.to_basic_dict())
        # print(house.to_basic_dict()['c_time'])

    data = dict(houses=houses_li)

    return jsonify(errno=RET.OK, errmsg='sucess get user houses', data=data)


@api1.route('/houses/<int:houseId>')
def get_house_detail(houseId):
    print(houseId)

    # 获取用户id用来之后判断，如果登陆用户则不能 预定 自己的房子
    # 好像并没有用上
    user_id = session.get('user_id', '-1')

    if not houseId:
        return jsonify(errno=RET.PARAMERR, errmsg="参数确实")


    # 从redis中取出数据
    try:
        house_json = redis_store.get('house_json_{}'.format(houseId))
    except Exception as e:
        current_app.logger.error(e)
        house_json = None

    if house_json:
        current_app.logger.info('hit house detail redis')
        rep_body = '{"errmsg": "OK", "errno": %s, "data": {"house": %s, "user_id": %s}}' % (RET.OK, house_json.decode(), user_id)

        return rep_body, 200, {"Content-Type": "application/json"}

    try:
        house = House.query.get(houseId)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='get house detail db err')

    if not house:
        return jsonify(errno=RET.NODATA, errmsg='get house detail no db err')

    # 获取评论时也需要查询数据库
    try:
        house_dict = house.to_detail_dict()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='get comments err from db')

    if house_dict is None:
        return jsonify(errno=RET.NODATA, errmsg='get index houses err')
    house_json = json.dumps(house_dict)

    #  将房子细节信息存入 redis
    try:
        redis_store.setex('house_json_{}'.format(houseId), constants.HOUSE_DETAIL_EXPIRE_TIMES, house_json)
    except Exception as e:
        current_app.logger.error(e)

    rep_body = '{"errmsg": "OK", "errno": %s, "data": {"house": %s, "user_id": %s}}' % (RET.OK, house_json, user_id)

    return rep_body, 200, {"Content-Type": "application/json"}


# GET /api/v1.0/houses?aid=6&sd=2020-2-13&ed=2020-2-14&sk=new&p=1
# 当查询条件很多时，总结
# 1 先判断aid,是否在给定区域内，时间格式是否正确，页码是否可以转换成整数，（排序条件没判断，因为默认可以设置成new）
# 2 构建查询条件列表，area id条件，时间冲突的房子id
# 3 使用查询条件后，排序，这时只需要生成查询语句，不查询数据库，不用捕获异常
# 4 构建分页page_obj = house_query.paginate(page=p, per=page, error_out=False)
# 5 获取当前页面的数据，及总页数，
# houses_li = page_obj.items
# total_page= page_obj.pages

@api1.route('/houses')
def get_house_list():
    params = request.args
    # print('params:', params)
    aid = params.get('aid', "")
    sd = params.get('sd', "")
    ed = params.get('ed', "")
    sk = params.get('sk', "new")
    p = params.get('p', "")

    # 转换传过来的时间格式为datetime类型
    try:
        if sd:
            sd_format = datetime.datetime.strptime(sd, "%Y-%m-%d")
        if ed:
            ed_format = datetime.datetime.strptime(ed, "%Y-%m-%d")
        if sd and ed:
            # 等于号表示，即使开始和结束时间相同，也可查出结果
            assert sd_format <= ed_format
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='datetime format err')


    # 判断区域id是否在数据库当中
    if aid:
        try:
            area = Area.query.get(aid)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="日期参数有误")
        else:
            if area is None:
                return jsonify(errno=RET.PARAMERR, errmsg="日期参数有误")


    # 检查分页条件
    try:
        p = int(p)
    except Exception as e:
        current_app.logger.error(e)
        p = 1


    # 从redis中取出缓存的某一页数据
    try:
        data_json = redis_store.hget("houses_{}_{}_{}_{}".format(aid, sd, ed, sk), p)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if data_json:
            current_app.logger.info('hit page houses from redis')
            return data_json, 200, {"Content-Type": "application/json"}

    # 过滤条件的参数列表
    filter_conditions = []

    # 添加订单过滤条件
    # 获取与订单时间冲突的数据
    conflict_orders = None

    try:
        if sd and ed:
            # 查询冲突的订单
            # 这个条件包含3种情况
            conflict_orders = Order.query.filter(Order.begin_date <= ed, Order.end_date >= sd).all()
        elif sd:
            conflict_orders = Order.query.filter(Order.end_date >= sd).all()
        elif ed:
            conflict_orders = Order.query.filter(Order.begin_date <= ed).all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    if conflict_orders:
        conflict_house_ids = [order.house_id for order in conflict_orders]
        if conflict_house_ids:
            filter_conditions.append(House.id.notin_(conflict_house_ids))

    # 添加区域条件
    # 实际上列表中多的是一个表达式
    # 等价于House.area_id.__eq__(1),这个方法被重新实现了
    # 可以查看方法dir(House.area_id)

    if aid:
        filter_conditions.append(House.area_id == aid)


    # # 测试查询条件
    # # id
    # houses = House.query.filter(House.area_id == aid).order_by(House.price.asc()).all()
    # print('测试条件id:', houses)
    # # 时间
    # houses = House.query.filter(House.id.notin_(conflict_house_ids)).order_by(House.price.asc()).all()
    # print('测试条件时间:', conflict_house_ids, houses)


    # 添加排序条件
    # 排序时只是获得查询条件，没有查询数据库，所以可以不加异常处理
    if sk == "booking":
        try:
            house_query = House.query.filter(*filter_conditions).order_by(House.order_count.desc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='house db order by order_count err')

    elif sk == "price-inc":
        try:
            house_query = House.query.filter(*filter_conditions).order_by(House.price.asc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='house db order by price asc')
    elif sk == "price-des":
        try:
            house_query = House.query.filter(*filter_conditions).order_by(House.price.desc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='house db order by price desc')
    else:
        #默认通过房子发布时间排序， "new"
        try:
            house_query = House.query.filter(*filter_conditions).order_by(House.create_time.desc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='house db order by creat_time desc')

    # print('house_query_all:', house_query.all())

    # 分页
    page_obj = None
    try:
        # 关闭自动的错误输出
        page_obj = house_query.paginate(page=p, per_page=constants.HOUSE_LIST_PAGE_CAPACITY, error_out=False)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="paginate err")

    # 获取当前页面数据
    if page_obj:
        house_li = page_obj.items
        houses = [house.to_basic_dict() for house in house_li]
        # print('houses:', len(houses), houses)

    # 获取总页数
    total_page = page_obj.pages

    data_dict = dict(errno=RET.OK, errmsg='OK', data={"total_page": total_page, "houses": houses, "current_page": p})
    data_json = json.dumps(data_dict)
    page_houses = "houses_{}_{}_{}_{}".format(aid, sd, ed, sk)

    if p <= total_page:
        # 将某一页的房子存入redis
        try:
            # redis_store.hset(page_houses, p, data_json)
            # redis_store.expire(page_houses, constants.PAGE_HOUSES_DATA_EXPIRE_TIMES)

            # 创建redis管道，可以一次执行多条语句
            pipeline = redis_store.pipeline()

            # 开启记录多个语句
            pipeline.multi()

            pipeline.hset(page_houses, p, data_json)
            pipeline.expire(page_houses, constants.PAGE_HOUSES_DATA_EXPIRE_TIMES)

            # 执行多条语句
            pipeline.execute()
        except Exception as e:
            current_app.logger.error(e)

    return data_json, 200, {"Content-Type": "application/json"}




