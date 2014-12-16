#coding=utf8

from flask import render_template, session, current_app, Blueprint

from .models import db
from .models import User

bp_test = Blueprint("test", __name__)
@bp_test.route('/')
@bp_test.route('/index/')
def index():
    session['tt'] = 'test'
    current_app
    test_user = User('gausszh', 'gauss.zh@gmail.com')
    print len(User.query.all())
    # db.session.commit()
    return render_template("index.html")