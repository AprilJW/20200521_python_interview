from flask import request, jsonify, current_app, session
from .. utils.response_code import RET
import re
from .. import redis_store, db, constants
from ..models import User
from sqlalchemy.exc import IntegrityError
from . import api1
print(type(request))


@api1.route('/sessions', methods=['POST'])
def login():
    req_dict = request.get_json()
    # print('login_req_dict:', req_dict)

    mobile = req_dict.get('mobile')
    password = req_dict.get('password')
    print('mobile:', mobile)
    print('password:', password)

    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='login params are incomplete')

    if not re.match(r'1[356789]\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='login in mobile not match')

    user_ip = request.remote_addr
    print("user_ip:", user_ip)
    try:
        access_num = redis_store.get('access_num_{}'.format(user_ip))
    except Exception as e:
        current_app.logger.error(e)

    if access_num is not None and int(access_num) >= constants.USER_LOGIN_LIMIT_TIMES:
        # print('access_num:', access_num, type(access_num), int(access_num))
        return jsonify(errno=RET.REQERR, errmsg='login after seconds')

    try:
        user_obj = User.query.filter_by(mobile=mobile).first()
        # print(user_obj)

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='query user from mysql err')

    if user_obj is None:
        return jsonify(errno=RET.LOGINERR, errmsg='user not register')

    if not user_obj.check_password(password):
        try:
            # redis的incr可以对字符串类型的数字数据进行加一操作，如果数据一开始不存在，则会初始化为1
            # 过期时间解释：
            # 如果第1次验证失败，则过期时间设置为30s, 如果第2次验证失败过期时间也为30s,第3次同样的道理
            # 当登陆超过第3次时，没执行到设置时间这一行，就返回，30s的过期时间开始生效。30s后，redis中的
            # 数据删除，用户则可以再次进行验证。
            redis_store.incr('access_num_{}'.format(user_ip))
            redis_store.expire('access_num_{}'.format(user_ip), constants.USER_LOGIN_LIMIT_SECONDS)

        except Exception as e:
            current_app.logger.error(e)

        return jsonify(errno=RET.LOGINERR, errmsg='user name or password err err err')

    session['user_id'] = user_obj.id
    session['name'] = user_obj.name
    session['mobile'] = mobile

    return jsonify(errno=RET.OK, errmsg='login sucess')


@api1.route('/users', methods=['POST'])
def register():
    req_dict = request.get_json()
    print('req_dict:', req_dict)

    mobile = req_dict.get('mobile')
    # image_code = req_dict.get('image_code')
    sms_code = req_dict.get('sms_code')
    password = req_dict.get('password')
    password2 = req_dict.get('password2')

    if not all([mobile, sms_code, password, password2]):
        return jsonify(errno=RET.PARAMERR, errmsg='register params are incomplete')

    if not re.match(r'1[34578]\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='mobile format err')

    if password != password2:
        return jsonify(errno=RET.PARAMERR, errmsg='password not match')

    try:
        real_sms_code = redis_store.get("mobile_verify_code_{}".format(mobile))
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='redis err')

    if real_sms_code is None:
        return jsonify(errno=RET.NODATA, errmsg='sms code expired')

    # # 如果想删除短信验证码，保证这个验证码只能用一次，可以在这里操作
    # try:
    #     redis_store.delete('mobile_verify_code_'.format(mobile))
    # except Exception as e:
    #     current_app.logger.error(e)
    #
    if real_sms_code != sms_code.encode():
        print('real_sms_code:', real_sms_code, sms_code)
        return jsonify(errno=RET.PARAMERR, errmsg='sms code err')

    # 注册的后端逻辑
    user = User(name=mobile, mobile=mobile, password=password)
    user.password = password

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAEXIST, errmsg='user already register')
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='添加用户异常')

    session['user_id'] = user.id
    session['name'] = user.name
    session['mobile'] = mobile

    return jsonify(errno=RET.OK, errmsg='register sucess')


@api1.route('/session', methods=['GET'])
def check_login():
    name = session.get('name')
    if name is not None:
        return jsonify(errno=RET.OK, errmsg='true', data={"name": name})
    else:
        return jsonify(errno=RET.SESSIONERR, errmsg='false')


@api1.route('/session', methods=['DELETE'])
def logout():
    # 本来csrf_token是存在于cookie当中的，但是session也存在于cookie当中，所以
    # csrf_token就存在于session当中，在退出时需要保留csrf_token，
    csrf_token = session.get('csrf_token')
    session.clear()
    session['csrf_token'] = csrf_token
    return jsonify(errno=RET.OK, errmsg='logout sucess')






