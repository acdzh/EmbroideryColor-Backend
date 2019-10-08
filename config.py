import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = "https://ecre.xyz"
    AVATAR_HOST = "{}/static/avatar".format(HOST)
    AVATAR_DIR = './static/avatar'
    FILE_HOST = "{}/static/files".format(HOST)
    FILE_DIR = "./static/files"

    LIB_HOST = "{}/static/lib".format(HOST)
    LIB_DIR = "./static/lib"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False


# 开发环境的配置
class DevelopmentConfig(Config):
    DEBUG = True
    # 数据库URI
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/EmbroideryColor'


class TestingConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(basedir, 'data.sqlite')


# 生产环境的配置
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/EmbroideryColor'


# 初始化app实例时对应的开发环境声明
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
    'basic': Config
}