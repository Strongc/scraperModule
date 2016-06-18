# !/usr/bin/env python
# -*- coding: utf-8 -*-    # import system default encoding
from __future__ import print_function,unicode_literals    # import features of Python 3


import time


def printTime(func):
    def _deco(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print('time:',func.__name__,end-begin)
        return func
    return _deco

@printTime
def func():
    time.sleep(1)
    
if __name__=="__main__":
    func()