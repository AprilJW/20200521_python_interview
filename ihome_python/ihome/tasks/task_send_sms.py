from celery import Celery
from ihome.libs.yuntongxun.sms import CCP
celery_app = Celery('celery_app',
                    broker='redis://172.16.177.160:6379/1')


@celery_app.task
def send_sms(to, datas, temp_id):
    ccp = CCP()
    ccp.send_template_sms(to, datas, temp_id)


# celery开启的命令 日志级别为info
# celery -A ihome.tasks.task_send_sms worker -l info

