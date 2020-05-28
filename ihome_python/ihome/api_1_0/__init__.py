from flask import Blueprint

api1 = Blueprint('api_1_0', __name__, url_prefix='',)
print(api1, type(api1))
print(__name__)

from . import demo, verify_code, passport, profile, houses, pay
# from .demo import index
# from .verify_code import get_image_code, get_sms_code
# from .passport import register
