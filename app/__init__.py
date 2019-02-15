import os

from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config, config

db = SQLAlchemy()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    @app.route('/')
    def index():
        return 'Hello World'

    from app.submit import submit_views
    app.register_blueprint(submit_views, url_prefix='/submit')

    return app
