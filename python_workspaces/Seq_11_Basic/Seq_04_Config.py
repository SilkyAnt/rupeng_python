# 基本（共有）配置
class BaseConfig():
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '419795232'
    MAIL_PASSWORD = 'xcywimnfskinbhbj'


# 测试的时候使用的配置信息
class TestConfig(BaseConfig):
    JLP = 3


# 开发的时候使用的配置信息
class DevelopConfig(BaseConfig):
    JLP = 3000


config = {
    'development': DevelopConfig,
    'testing': TestConfig,
    'default': DevelopConfig
}
