from flask import Blueprint

submit_views = Blueprint('submit', __name__)

from app.submit import views
