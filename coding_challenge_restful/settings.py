import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    COUNTRY_NAME = 'INDIA'
    COUNTRY_TIME_ZONE = 'Asia/Kolkata'
    DATABASE_URL = os.environ.get('DATABASE_URL', default='postgresql://fulfilio:fulfilio@localhost:9011/fulfilio')
    CLOUDAMQP_URL = os.environ.get('CLOUDAMQP_URL', default='amqp://roczasps:1SmPpVkg2pdx_k2MMX8dZRQmz_x-Ovw_@llama'
                                                            '.rmq.cloudamqp.com/roczasps')
    CELERY_BACKEND = "db+" + DATABASE_URL
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', default='None')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY', default='None')
    AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY = AWS_SECRET_KEY
