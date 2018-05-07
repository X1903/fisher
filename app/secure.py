# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

"""
记录开发环境和生产环境相同的配置，涉及机密信息
"""

# pipenv install cymysql

PER_PAGE = 15


DEBUG = True

# SERVER_NAME = '127.0.0.1:8888'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:q8022761@127.0.0.1:3306/fisher'
SECRET_KEY = 'QWE34rsdssd32dfsdRTYUIOPKJHGFDFGdsfgHYU'