# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from app.models.base import db
from sqlalchemy import Column, Integer, String, Boolean, Float

class User(db.Model):

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=Float)
    phone = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))