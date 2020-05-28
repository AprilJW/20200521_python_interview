# -*- coding: utf-8 -*-

from qiniu import Auth, put_data, etag, urlsafe_base64_encode
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'p4HYUStcASYFjqWRJ_D7t5GB9_2JjJ7DPaibyCVS'
secret_key = '9m2zXI6EaBxjJkNDJ_Euw427DVhU2O_im6Uz8RmH'


def storage(file_data):
    """
    上传文件到七牛
    :param file_data: 要上传的文件数据
    :return:
    """
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'ihome-python-jw'

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)

    ret, info = put_data(token, None, file_data)

    # print(info)
    # print("*"*10)
    # print(ret)
    if info.status_code == 200:
        # 表示上传成功, 返回文件名
        # 也可以返回 0
        return ret.get("key")
    else:
        # 上传失败
        # 也可以返回 -1
        raise Exception("上传七牛失败")


if __name__ == '__main__':
    url_test = '/Users/jw/Projects/ihome_python/ihome/static/images/landlord01.jpg'
    # qiniu = 'http://q5dnq6v4k.bkt.clouddn.com/'
    with open(url_test, "rb") as f:
        file_data = f.read()
        storage(file_data)
