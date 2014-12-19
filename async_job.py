#coding=utf8

import time
from flask.ext.rq import job

@job
def echo(a, b):
    time.sleep(1)
    return a + b