#coding=utf8

from myapp import app

if __name__ == '__main__':
    # from myapp import db
    # db.create_all()
    app.run(debug=True)