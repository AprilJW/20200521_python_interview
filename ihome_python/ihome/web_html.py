from flask import Blueprint, current_app, make_response
from flask_wtf import csrf


html = Blueprint('web_html', __name__)


# 127.0.0.1:5000/favicon.ico   # 浏览器认为的网站标识， 浏览器会自己请求这个资源
@html.route("/<re(r'.*'):html_filename>")
def get_html(html_filename):

    if not html_filename:
        html_filename = 'index.html'

    if html_filename != 'favicon.ico':
        html_filename = 'html/' + html_filename

    csrf_token = csrf.generate_csrf()

    resp = make_response(current_app.send_static_file(html_filename))
    print(current_app.send_static_file(html_filename), type(current_app.send_static_file(html_filename)))

    resp.set_cookie('csrf_token', csrf_token)

    return resp