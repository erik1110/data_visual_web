POSTGRES = {
    'user': 'postgres',
    'password': 'PASSWORD',
    'db': 'erik',
    'host': 'localhost',
    'port': '5432',
    }

class Config(object):
    APP_TITLE = 'data_visual_POC'
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'enydasdasdasfM2dhASDdsadadfdgeANhdcdfgjWvEsbPFuQpMjf'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True