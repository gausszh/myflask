#coding=utf8

from async_job import enqueue_job
import time


def test_method(a, b):
    time.sleep(3)
    return a + b

ret = enqueue_job(test_method, 2, 4)
print ret
time.sleep(4)
print ret.result