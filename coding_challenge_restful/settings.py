import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    COUNTRY_NAME = 'INDIA'
    COUNTRY_TIME_ZONE = 'Asia/Kolkata'
    APP_REQUEST_AUTH_SECRET = "MySecretKeyForJwtToken"
    JWT_ACCESS_TOKEN_EXPIRES = 5
    DATABASE_URL = os.environ.get('DATABASE_URL', default='postgresql://fulfilio:fulfilio@localhost:9011/fulfilio')
    CLOUDAMQP_URL = os.environ.get('CLOUDAMQP_URL', default='amqp://ifhzzjcg:CwMA3k...@golden-kangaroo.rmq.cloudamqp'
                                                            '.com/ifhzzjcg ')
