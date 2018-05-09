# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer
db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True    # sqlalchemy不会认为创建Base表了
    status = Column(SmallInteger, default=1)   # 是否隐藏删除


    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


