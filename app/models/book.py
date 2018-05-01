# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# sqlalchemy
# Flask_SQLAlchemy
# WTFORMS
# Flask_WTFORMS

# Flask
# werkzeug  # 实现路有分配

# pipenv graph

from sqlalchemy import Column, Integer, String, INTEGER
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Cdoe First  专注业务模型的设计, 而不是专注数据库设计
# 数据库只是用来存储数据的, 它的表关系应该由我们的业务来决定

# 业务逻辑是应该写在MVC里的那一层??  业务逻辑最好写在model层里面

class Book(db.Model):
    __tablename__ = 'tb_book'

    id = Column(INTEGER, primary_key=True, autoincrement=True, comment='自增主键')  # ID 主键, 自增长
    title = Column(String(50), nullable=False, comment='图书名称')                  # 标题, 不能为空
    author = Column(String(30), nullable=True, default='未名', comment='作者')      # 作者,可以为空,默认值'未名'
    binding = Column(String(20), comment='装帧')                                   # 装帧的版本, 精装还是平装?
    publisher = Column(String(50), comment='出版社')                               # 出版社
    price = Column(String(20), comment='价格')                                     # 价格
    pages = Column(INTEGER, comment='页数')                                        # 页数
    pubdate = Column(String(20), comment='出版年')                                 # 出版的年月
    isbn = Column(String(15), nullable=False, unique=True, comment='唯一isbn号')   # 图书的编号, 不能为空,不能重复
    summary = Column(String(1000), comment='内容简介')                             # 图书的简介
    image = Column(String(50), comment='图片地址')                                 # 图书的封面

    # MVC M Model  只有数据 = 数据表
    # ORM 对象关系映射 Code First

    def sample(self):
        pass