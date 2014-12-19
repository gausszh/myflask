#coding=utf8
from redis import Redis
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib import rediscli

from myapp.models.home import User
from myapp.models import Session


class UserView(BaseView):
    """docstring for UserView"""
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

    @expose('/user/')
    def show_user(self):
        return self.render('admin/index.html')

admin = Admin(name="my admin")
admin.add_view(UserView(name="User", endpoint="user", category="test"))
admin.add_view(UserView(name="login", endpoint="login", category="test"))
admin.add_view(ModelView(User, Session))
admin.add_view(rediscli.RedisCli(Redis(), name="tt"))