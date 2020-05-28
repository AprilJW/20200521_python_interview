class Config:

    SECRET_KEY = "XHS999*Y9dfs9cshd9"
    SESSION_TYPE = 'filesystem'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql://jw:7709@172.16.177.160:3306/ihome_python"


    REDIS_HOST = '172.16.177.160'
    REDIS_PORT = 6379


class DevelopmentConfig(Config):
    DEBUG = False


class ProductionConfig(Config):
    pass


config_map = {'develop': DevelopmentConfig,
              'produce': ProductionConfig,
              }

