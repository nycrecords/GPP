import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    NYC_GOV_BASE = 'www1.nyc.gov'

    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL'))

    # Redis Settings
    REDIS_HOST = os.environ.get('REDIS_HOST') or 'localhost'
    REDIS_PORT = os.environ.get('REDIS_PORT') or '6379'
    CELERY_REDIS_DB = 0
    SESSION_REDIS_DB = 1
    UPLOAD_REDIS_DB = 2
    EMAIL_REDIS_DB = 3

    # Celery Settings
    CELERY_BROKER_URL = 'redis://{redis_host}:{redis_port}/{celery_redis_db}'.format(
        redis_host=REDIS_HOST,
        redis_port=REDIS_PORT,
        celery_redis_db=CELERY_REDIS_DB
    )

    # Flask-Mail Settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', "True") == "True"
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = os.environ.get('MAIL_SUBJECT_PREFIX')
    MAIL_SENDER = os.environ.get('MAIL_SENDER')


class DevelopmentConfig(Config):
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 2525
    MAIL_USE_TLS = False
    MAIL_SUBJECT_PREFIX = '[GPP Development]'
    MAIL_SENDER = 'GPP - Dev Admin <donotreply@records.nyc.gov>'


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
