# coding=utf8

from flask import render_template, Blueprint

from myapp.forms.test import LoginForm

bp_home = Blueprint('home', __name__)

@bp_home.route('/', methods=['GET', 'POST'])
@bp_home.route('/index/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template("index.html", ok=True, form=form)
    return render_template("index.html", form=form)
