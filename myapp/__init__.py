#coding=utf8

from flask import Flask

from models import db
from utils import assets
from views import bp_test


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config')
    app.register_blueprint(bp_test, url_prefix="/test")
    db.init_app(app)
    assets.init_app(app)
    
    return app

app = create_app()

