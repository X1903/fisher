# _*_ coding:utf-8 _*_
from flask import Flask
from app.models.book import db

__author__ = 'Xbc'

def create_app():
    # app = Flask(__name__, static_folder='', static_path='')
    # app = Flask(__name__, template_folder='web/templates')
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    # 初始化蓝图
    register_blueprint(app)

    # 绑定数据库
    db.init_app(app)


    # 下面两种方法都可以创建数据库
    db.create_all(app=app)

    # with app.app_context():
    #     db.create_all()

    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)