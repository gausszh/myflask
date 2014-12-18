#coding=utf8

from flask import Flask
from myapp.views.home import bp_home
from myapp.utils import assets

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    app.register_blueprint(bp_home, url_prefix="/home")
    assets.init_app(app)
    return app
