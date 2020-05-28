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

@api1.route("/orders/<int:order_id>/payment", methods=['POST'])
@login_required
def order_pay(order_id):

    user_id = g.user_id

    # 判断订单号，用户是否是当前用户，及订单的状态是否是处于待支付状态
    try:
        order = Order.query.filter(Order.id == order_id, Order.user_id == user_id, Order.status == "WAIT_PAYMENT").first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="order pay Order db error")

    if order is None:
        return jsonify(errno=RET.NODATA, errmsg="order pay nodata")

    with open(os.path.join(os.path.dirname(__file__), "keys/app_private_key.pem")) as f:
        app_private_key_string = f.read()

    print('path:', os.path.join(os.path.dirname(__file__), "keys/alipay_public_key.pem"))
    with open(os.path.join(os.path.dirname(__file__), "keys/alipay_public_key.pem")) as f:
        alipay_public_key_string = f.read()

    # 创建支付宝sdk的工具对象
    alipay_client = AliPay(
        appid="2021001127677101",
        app_notify_url=None,  # 默认回调url
        # 可以适应不同的操作系统
        app_private_key_string=app_private_key_string,  # 私钥
        alipay_public_key_string=alipay_public_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False
)

    # 手机网站支付，需要跳转到https://openapi.alipaydev.com/gateway.do? + order_string
    order_string = alipay_client.api_alipay_trade_wap_pay(
        out_trade_no=order.id,  # 订单编号
        total_amount=str(order.amount / 100.0),  # 总金额
        subject=u"爱家租房订单编号： %s" % order.id,  # 订单标题
        return_url="http://127.0.0.1:5000/payComplete.html",  # 返回的连接地址
        notify_url=None  # 可选, 不填则使用默认notify url
    )

    # 构建让用户跳转的支付连接地址
    pay_url = constants.ALIPAY_URL_PREFIX + order_string
    return jsonify(errno=RET.OK, errmsg="OK", data={"pay_url": pay_url})

