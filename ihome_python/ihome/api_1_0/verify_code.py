from . import api1
from .. import redis_store
from ..utils.captcha.captcha import captcha
from ..utils.response_code import RET, error_map
from .. import constants
from flask import current_app, jsonify, make_response, request
from .. import db
from ..models import User
from ..libs.yuntongxun.sms import CCP
import random
from ..tasks.task_send_sms import send_sms



@api1.route('/image_codes/<image_code_id>')
def get_image_code(image_code_id):
    """
    :param image_code_id: 图片验证码
    :return:
    """
    name, text, image_data = captcha.generate_captcha()

    try:
        # redis_store.set('image code {}'.format(image_code_id), text)
        # redis_store.expire('image code {}'.format(image_code_id), constants.IMAGE_CODE_REDIS_EXPIRES)
        redis_store.setex('image_code_{}'.format(image_code_id), constants.IMAGE_CODE_REDIS_EXPIRES, text)
        # a = redis_store.get('image_code_{}'.format(image_code_id))
        # print('a:', a)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg=error_map[RET.DBERR])

    # print('image_data:', type(image_data))

    resp = make_response(image_data)
    resp.headers['Content-Type'] = 'image/jpg'
    return resp



# 'image_code_466ad3ad-3b9c-42e0-a1f4-14eec115d35b'
# 'image_code_466ad3ad-3b9c-42e0-a1f4-14eec115d35b'

# get /sms_codes/<mobile_phone>?image_code_id=xxx&image_code=xxx
@api1.route("/sms_codes/<re(r'1[34578]\d{9}'):mobile_phone>")
def get_sms_code(mobile_phone):
    # 获取参数
    # image_code_id = request.args.get('image_code_id')
    # image_code = request.args.get('image_code')
    # print('request.args:', dict(request.args))

    # 参数检查
    # if not all([image_code_id, image_code]):
    #     return jsonify(errno=RET.PARAMERR, errmsg='paramerr is incomplete')

    # 后端逻辑
    # 点击发送短信之前，校验图片验证码
    # try:
    #     image_code_id_join = 'image_code_{}'.format(image_code_id)
    #     print('image_code_id_join:', image_code_id_join)
    #     real_image_code = redis_store.get(image_code_id_join)
    # except Exception as e:
    #     current_app.logger.error(e)
    # else:
    #     print('real_image_code:', real_image_code)
    #     # real_image_code = 'hezn'.encode()
    #     if real_image_code is None:
    #         return jsonify(errno=RET.NODATA, errmsg='verification code expired')

        # # # 删除图片片验证码, 一个验证码只能使用一次
        # # elif real_image_code:
        # #     try:
        # #         redis_store.delete('image_code_{}'.format(image_code_id))
        # #     except Exception as e:
        # #         current_app.logger.error(e)
        # elif real_image_code.lower() != image_code.encode().lower():
        #     print(image_code.lower(), real_image_code.lower())
        #     return jsonify(errno=RET.PARAMERR, errmsg='verification code not match')

    # 判断手机号码是否在60秒之内重新发送的，需要在查询mysql数据库之前完成
    try:
        mobile_verify_code_interval = redis_store.get('send_verify_code_interval')
    except Exception as e:
        current_app.logger.error(e)
    else:
        if mobile_verify_code_interval is not None:
            return jsonify(errno=RET.REQERR, errmsg='Request after 60 seconds')

    # 发送短信验证码之前判断用户名是手机号是否已经注册
    try:
        # user = db.session(User).filter_by(mobile=mobile_phone).first()
        user = User.query.filter_by(mobile=mobile_phone).first()
    except Exception as e:
        current_app.logger.error(e)
    else:
        # 在数据库没有发生异常，才会执行else，即user的值为None，或者对象
        # 如果数据库发生了异常，user等号右边没有被执行，user没有定义，不应该
        # 执行else后面的条件判断
        if user is not None:
            return jsonify(errno=RET.DATAEXIST, errmsg='User already exists')


    verify_code = str(random.randint(1000, 9999))
    try:
        redis_store.setex('mobile_verify_code_{}'.format(mobile_phone), constants.SMS_CODE_EXPIRES, verify_code)
        redis_store.setex('send_verify_code_interval', constants.SEND_VERIFY_CODE_INTERVAL, 1)
    except Exception as e:
        current_app.logger.error(e)

    # ccp = CCP()
    # ret = ccp.send_template_sms(mobile_phone, [verify_code, str(constants.SMS_CODE_EXPIRES/60)], 1)
    # if ret == 0:
    #     return jsonify(msgno=RET.OK, msg='sucess send')
    # else:
    #     return jsonify(errno=RET.DBERR, msg='fail send')


    # 使用celery异步发送短信, delay函数调用后立即返回（非阻塞）
    result_obj = send_sms.delay(mobile_phone, [verify_code, str(constants.SMS_CODE_EXPIRES/60)], 1)
    print(result_obj.id)


    # 通过异步对象的get方法，获取异步的结果，默认get方法是阻塞的
    ret = result_obj.get()
    print('task send sms ret={}'.format(ret))

    return jsonify(msgno=RET.OK, msg='sucess send')


    # 返回








# 处理请求
# 验证信息
# 业务逻辑
# 1 生成验证码
# 2 验证吗保存到redis中
# 返回