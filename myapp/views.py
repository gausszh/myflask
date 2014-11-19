#coding=utf8

from . import app

@app.route('/')
@app.route('/index/')
def index():
	return 'index %s' % app.config['UPPER'] 