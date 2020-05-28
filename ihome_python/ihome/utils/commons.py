from werkzeug.routing import BaseConverter
import functools
from flask import session, g, jsonify
from .response_code import RET


# 静态文件匹配的转换器
# 获取验证码时的转换器
class ReConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex


# define verify login decorator
def login_required(view_func):

    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id is not None:
            # 将user_id保存到g对象中，在视图函数中可以通过g对象获取保存数据
            # 因为这个装饰器和视图函数需要同时使用，所以用到了g对象
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            return jsonify(errno=RET.SESSIONERR, errmsg='please login first')

    return wrapper