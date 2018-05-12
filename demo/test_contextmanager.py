# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from contextlib import contextmanager

@contextmanager
def book_mark():
    print('<', end='')
    yield
    print('>', end='')

with book_mark():
    print('且将生活一饮而尽', end='')