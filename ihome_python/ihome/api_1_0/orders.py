from . import api1
from flask import g, current_app, request, jsonify, session
from ..utils.commons import login_required
from ..utils.image_storage import storage
from ..utils.response_code import RET
from ..models import User, Area, House, HouseImage, Facility, Order
from .. import constants, db, redis_store

import json
import os
from sqlalchemy import and_, or_
import datetime
from alipay import AliPay


@api1.route("/orders", methods=["POST", "GET", "PUT"])
@login_required
def save_order():
    user_id = g.user_id  # 加了装饰器后用户一定存在，不用再单独判断

    # 获取参数
    order_data = request.get_json()
    if not order_data:
        return jsonify(errno=RET.PARAMERR, errmsg="save order paramerr 1")

    house_id = order_data.get("house_id")
    start_date_str = order_data.get("start_date")
    end_date_str = order_data.get("end_date")

    if not all([house_id, start_date_str, end_date_str]):
        return jsonify(errno=RET.PARAMERR, errmsg="save order paramerr 2")

    # 日期格式检查
    try:
        start_date = datetime.datetime.strptime(start_date_str)
        end_date = datetime.datetime.strptime(end_date_str)

        assert start_date <= end_date

        days = (end_date - start_date).days + 1

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="date format paramerr")

    # 检查房子是否存在
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="save order db error")

    if not house:
        return jsonify(errno=RET.NODATA, errmsg="no data")

    # 判断房子中的主人是不是用户自己，如果是自己则不能定自己的房子
    if house.user_id == user_id:
        return jsonify(errno=RET.ROLEERR, errmsg='cannot order yourself house')

    # 判断订单时间是否冲突
    try:
        count = Order.query.filter(Order.house_id == house_id, Order.begin_date <= end_date,
                           Order.end_date >= start_date).count()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="db error")

    # 如果一个数据都没查到count = 0, 不是None
    print('count:', count)

    if count > 0:
        return jsonify(errno=RET.DATAERR, errmsg="house already is ordered")

    amount = days * house.price

    # 保存订单数据
    order = Order(
        house_id=house_id,
        user_id=user_id,
        begin_date=start_date,
        end_date=end_date,
        days=days,
        amount=amount,
        house_price=house.price
    )

    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.roll_back()
        return jsonify(errno=RET.DBERR, errmsg="save order in db error")

    return jsonify(errno=RET.OK, errmsg="OK", data={"order_id": order.id})


# 将查询我的订单和房东查询别人预订了自己房子的订单放到一起
# /api1/v1.0/user/orders?role=customer role=landlord
@api1.route("/user/orders", methods=['GET'])
@login_required
def get_user_orders():
    user_id = g.user_id

    role = request.args.get("role", "")
    if role == "landlord":
        try:
            user = User.query.filter_by(id=user_id).all()
            house_ids = [house.id for house in user.houses]
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="get user orders user db error")

        try:
            orders = Order.query.filter(Order.house_id.in_(house_ids)).order_by(Order.create_time.desc()).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="get user query order db error")

    else:
        try:
            orders = Order.query.filter(Order.user_id == user_id).order_by(Order.create_time.desc()).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="get user orders Order db error")

    orders_dict_list = []
    if orders:
        for order in orders:
            orders_dict_list.append(order.to_dict())

    return jsonify(errno=RET.OK, errmsg="OK", data={"orders": orders_dict_list})


@api1.route("/orders/<int: order_id>/status", methods=["PUT"])
@login_required
def accept_reject_order(order_id):
    user_id = g.user_id

    req_data = request.get_json()
    if not req_data:
        return jsonify(errno=RET.PARAMERR, errmsg="accept reject order paramerr")

    action = req_data.get("action")
    if action not in ("accept", "reject"):
        return jsonify(errno=RET.PARAMERR, errmsg="accept reject order action paramerr")

    try:
        order = Order.query.filter(Order.house.user_id == user_id, Order.id == order_id,
                                   Order.status == action).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="accept reject order query db error")

    if order is None:
        return jsonify(errno=RET.NODATA, errmsg="accept reject order no data")

    if action == "accept":
        order.status = "WAIT_PAYMENT"
    elif action == "reject":
        reason = req_data.get("reason")
        if not reason:
            return jsonify(errno=RET.PARAMERR, errmsg="accept reject order reason paramerr")
        order.comment = reason
        order.status = "REJECTED"

    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.roll_back()
        return jsonify(errno=RET.DBERR, errmsg=" accept reject order update db error")

    return jsonify(errno=RET.OK, errmsg="OK")


@api1.route("orders/<int:order_id>/comment", methods=["PUT"])
@login_required
def save_order_comment(order_id):
    user_id = g.user_id

    req_data = request.get_json()
    comment = req_data.get("comment")

    if not comment:
        return jsonify(errno=RET.PARAMERR, errmsg="save order comment paramerr")

    try:
        order = Order.query.filter(Order.id == order_id, Order.user_id == user_id,
                                   Order.status == "WAIT_COMMIT").first()
        # 订单评论完成后，house表中的订单数量需要加1
        house = order.house
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="无法获取订单数据")

    if not order:
        return jsonify(errno=RET.REQERR, errmsg="操作无效")

    try:
        order.status = "COMPLETE"
        order.comment = comment
        house.order_count += 1
        db.session.add(order)
        db.session.add(house)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="操作失败")

    # 评论完成后，因为之前redis当中也存了房子细节的缓存信息，所以需要清除缓存
    try:
        redis_store.delete("house_json_{}".format(order.house.id))
    except Exception as e:
        current_app.logger.error(e)

    return jsonify(errno=RET.OK, errmsg="OK")









