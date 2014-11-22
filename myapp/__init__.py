#coding=utf8

from flask import Flask

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config')

from .utils import assets
from .views import *