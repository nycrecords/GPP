from celery import Celery
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config, config

db = SQLAlchemy()
migrate = Migrate()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app import models

    db.init_app(app)
    migrate.init_app(app, db)

    from app.submit import submit_views
    app.register_blueprint(submit_views, url_prefix='/submit')

    return app
