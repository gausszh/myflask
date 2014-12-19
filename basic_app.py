#coding=utf8

import time

from flask import (Flask, request, make_response, session, abort,
                   render_template)
from flask.ext.rq import RQ, job

from async_job import echo

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.secret_key = "complex"
app.config['RQ_LOW_URL'] = 'redis://127.0.0.1:6379/2'
RQ(app)



@app.route('/netease/<name>/')
def index(name="cc"):
    # abort(500)

    # get 请求的参数
    age = request.args.get('age', 0, int)

    #### session
    # set
    session['session_1'] = 'netease'
    # get
    session_1 = session['session_1']

    #### cookies
    # get
    cookie_1 = request.cookies.get('cookie_1')
    # set 
    ret = 'hello world!<br> %s, age: %s' % (name, age)
    resp = make_response(ret)
    resp.set_cookie('cookie_1', 'cc')
    resp.set_cookie('cookie_2', 'netease', httponly=True)
    return resp


@app.route('/async/')
def fast_echo():
    job = echo.delay(2, 5)
    print job
    return str(job.result)


@app.errorhandler(500)
def server_error(error):
    return "sorry. server error", 500

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
