#coding=utf8


# from flask import Flask, request, make_response, escape, session, abort

# app = Flask(__name__)
# app.secret_key = "complex"

# @app.route('/netease/<name>/')
# def index(name="cc"):
#     # abort(500)

#     # get 请求的参数
#     age = request.args.get('age', 0, int)

#     #### session
#     # set
#     session['session_1'] = 'cc'
#     # get
#     session_1 = escape(session['session_1'])


#     #### cookies
#     # get
#     cookie_1 = request.cookies.get('cookie_1')
#     # set 
#     ret = 'hello world! %s, age: %s' % (name, age)
#     resp = make_response(ret)
#     resp.set_cookie('cookie_1', 'cc')
#     return resp

# @app.errorhandler(500)
# def server_error(error):
#     return "sorry. server error", 500

from myapp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
