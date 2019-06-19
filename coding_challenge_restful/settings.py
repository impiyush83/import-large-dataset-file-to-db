import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    COUNTRY_NAME = 'INDIA'
    COUNTRY_TIME_ZONE = 'Asia/Kolkata'
    DATABASE_URL = os.environ.get('DATABASE_URL', default='postgresql://fulfilio:fulfilio@localhost/fulfilio')
    CLOUDAMQP_URL = os.environ.get('CLOUDAMQP_URL', default='amqp://hehtklkb:r0hE-gCaRipvKlm49SyJwBF0lAQF3xZq@reindeer.rmq.cloudamqp.com/hehtklkb')
    CELERY_BACKEND = "db+" + DATABASE_URL
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY', default='None')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY', default='None')
    AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY = AWS_SECRET_KEY
