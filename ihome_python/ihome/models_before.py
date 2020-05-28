from ihome import db
from flask_sqlalchemy import SQLAlchemy
import datetime
# db:SQLAlchemy


class BaseModel(db.Model):

    create_time = db.Column(db.DateTime, default=datetime.datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())


class User(BaseModel, db.Model):

    __tablename__ = 'ihome_python_user_profile'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), unique=True, nullable=False)
    mobile = db.Column(db.String(11), unique=True, nullable=False)
    real_name = db.Column(db.String(32))
    id_card = db.Column(db.String(20))
    # 用户头像路径
    avatar_url = db.Column(db.String(128))

    # 在一表中，或者多表中写relationship
    houses = db.relationship('House', backref='user')
    orders = db.relationship('Order', backref='user')


# 房屋设施表，建立房屋与设施的多对多关系
# 没有设置id, 联合主键做id
house_facility = db.Table(
    'ihome_python_house_facility',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('house_id', db.Integer, db.ForeignKey('ihome_python_house_info.id')),
    db.Column('facility_id', db.Integer, db.ForeignKey('ihome_python_facility_info.id'))
)

class House(BaseModel):

    __tablename__ = 'ihome_python_house_info'

    id = db.Column(db.Integer, primary_key=True)
    # 在多表中建立外键
    user_id = db.Column(db.Integer, db.ForeignKey('ihome_python_user_profile.id'), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('ihome_python_area_info.id'), nullable=False)

    title = db.Column(db.String(64), nullable=False)  # 标题
    price = db.Column(db.Integer, default=0)  # 单价，单位：分
    address = db.Column(db.String(512), default="")  # 地址
    room_count = db.Column(db.Integer, default=1)  # 房间数目
    acreage = db.Column(db.Integer, default=0)  # 房屋面积
    unit = db.Column(db.String(32), default="")  # 房屋单元， 如几室几厅
    capacity = db.Column(db.Integer, default=1)  # 房屋容纳的人数
    beds = db.Column(db.String(64), default="")  # 房屋床铺的配置
    deposit = db.Column(db.Integer, default=0)  # 房屋押金
    min_days = db.Column(db.Integer, default=1)  # 最少入住天数
    max_days = db.Column(db.Integer, default=0)  # 最多入住天数，0表示不限制
    order_count = db.Column(db.Integer, default=0)  # 预订完成的该房屋的订单数
    index_image_url = db.Column(db.String(256), default="")  # 房屋主图片的路径

    facilities = db.relationship('Facility', secondary=house_facility)
    images = db.relationship('HouseImage')
    orders = db.relationship('Order', backref='house')


class Facility(BaseModel):

    __tablename__ = 'ihome_python_facility_info'

    id = db.Column(db.Integer, primary_key=True)  # 设施编号
    name = db.Column(db.String(32), nullable=False) # 设施名字


class Area(BaseModel):

    __tablename = 'ihome_python_area_info'

    id = db.Column(db.Integer, primary_key=True)  # 区域编号
    name = db.Column(db.String(32), nullable=False)  # 区域名字
    houses = db.relationship('House', backref='area')


class HouseImage(BaseModel):

    __tablename__ = "ihome_python_house_image"

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey("ihome_python_house_info.id"), nullable=False)  # 房屋编号
    url = db.Column(db.String(256), nullable=False)  # 图片的路径


class Order(BaseModel):

    __tablename__ = 'ihome_python_order_info'

    user_id = db.Column(db.Integer, db.ForeignKey('ihome_python_user_profile.id'), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house_info.id"), nullable=False)  # 预订的房间编号
    begin_date = db.Column(db.DateTime, nullable=False)  # 预订的起始时间
    end_date = db.Column(db.DateTime, nullable=False)  # 预订的结束时间
    days = db.Column(db.Integer, nullable=False)  # 预订的总天数
    house_price = db.Column(db.Integer, nullable=False)  # 房屋的单价
    amount = db.Column(db.Integer, nullable=False)  # 订单的总金额
    status = db.Column(  # 订单的状态
        db.Enum(  # 枚举     # django choice
            "WAIT_ACCEPT",  # 待接单,
            "WAIT_PAYMENT",  # 待支付
            "PAID",  # 已支付
            "WAIT_COMMENT",  # 待评价
            "COMPLETE",  # 已完成
            "CANCELED",  # 已取消
            "REJECTED"  # 已拒单
        ),
        default="WAIT_ACCEPT", index=True)  # 指明在mysql中这个字段建立索引，加快查询速度
    comment = db.Column(db.Text)  # 订单的评论信息或者拒单原因
    trade_no = db.Column(db.String(80))  # 交易的流水号 支付宝的

