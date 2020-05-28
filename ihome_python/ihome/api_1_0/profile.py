from . import api1
from flask import g, current_app, request, jsonify, session
from ..utils.commons import login_required
from ..utils.image_storage import storage
from ..utils.response_code import RET
from ..models import User
from .. import constants, db


@api1.route('/users/avatar', methods=['PUT', 'POST'])
@login_required
def set_user_avatar():
    image_file = request.files.get('avatar')
    if image_file is None:
        return jsonify(errno=RET.PARAMERR, errmsg='avatar not uploaded ')

    # 为什么没打开，直接读了
    image_data = image_file.read()
    print('image_data:', type(image_data))

    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg='avatar upload failed')

    try:
        User.query.filter_by(id=g.user_id).update({'avatar_url': file_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='avatar upload failed')

    avatar_url = constants.QINIU_URL_DOMAIN + file_name
    return jsonify(errno=RET.OK, errmsg='upload sucess', data={'avatar_url': avatar_url})


@api1.route('/users/name', methods=['PUT'])
@login_required
def change_user_name():

    user_id = g.user_id

    user_dict = request.get_json()
    if user_dict is None:
        return jsonify(errno=RET.PARAMERR, errmsg='user name para incomplete')

    user_name = user_dict.get('name')
    if user_name is None:
        return jsonify(errno=RET.PARAMERR, errmsg='please fill in the user name')

    try:
        User.query.filter_by(id=user_id).update({'name': user_name})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='user name update failed')

    session['name'] = user_name
    return jsonify(errno=RET.OK, errmsg='user name update sucess', data={'name': user_name})


@api1.route('/user', methods=['GET'])
@login_required
def get_user_profile():
    user_id = g.user_id

    try:
        user = User.query.filter_by(id=user_id).first()
    except Exception as e:
        current_app.logger.err(e)
        return jsonify(errno=RET.DBERR, errmsg='db query failed')

    if user is None:
        return jsonify(errno=RET.NODATA, errmsg='db query failed')

    return jsonify(errno=RET.OK, errmsg='query sucess', data=user.to_dict())


@api1.route('/users/auth', methods=['GET'])
@login_required
def get_user_auth():
    user_id = g.user_id

    try:
        user = User.query.filter_by(id=user_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='db query err')

    if user is None:
        return jsonify(errno=RET.DBERR, errmsg='db query err')

    return jsonify(errno=RET.OK, errmsg='query user sucess', data=user.auth_to_dict())


@api1.route('/users/auth', methods=['POST'])
@login_required
def set_user_auth():

    user_id = g.user_id

    req_data = request.get_json()
    if not req_data:
        return jsonify(errno=RET.PARAMERR, errmsg='auth param err')

    real_name = req_data.get('real_name')
    id_card = req_data.get('id_card')
    if not all([real_name, id_card]):
        return jsonify(errno=RET.PARAMERR, errmsg='auth user params incomplete')

    # 因为数据空中真实姓名和身份证号是唯一键，所以如果重复设置，也会抛出异常
    try:
        User.query.filter_by(id=user_id, real_name=None, id_card=None).\
            update({'real_name': real_name, 'id_card': id_card})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.err(e)
        return jsonify(errno=RET.DBERR, errmsg='updata auth err')

    return jsonify(errno=RET.OK, errmsg='auth sucess')

