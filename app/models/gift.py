# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from app.models.base import db, Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship


class Gift(Base):

    id = Column(Integer, primary_key=True)

    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))

    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey(''))
    isbn = Column(String(15), nullable=False)

    launched = Column(Boolean, default=False)  # 礼物是送出去


