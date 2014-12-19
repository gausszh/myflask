#!/usr/bin/env python
#coding=utf8

from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email


class LoginForm(Form):
    username = TextField("username", validators=[Required(), Email()])
    password = PasswordField("password", validators=[Required()])
