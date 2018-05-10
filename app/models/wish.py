# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.spider.yushu_book import YuShuBook
from app.models.base import Base


class Wish(Base):

    __tablename__ = 'with'

    id = Column(Integer, primary_key=True)

    uid = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('User')

    isbn = Column(String(13))

    launched = Column(Boolean, default=False)


