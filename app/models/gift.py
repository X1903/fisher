# _*_ coding:utf-8 _*_
__author__ = 'Xbc'


from flask import current_app
from collections import namedtuple
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):

    id = Column(Integer, primary_key=True)

    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))

    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey(''))
    isbn = Column(String(15), nullable=False)

    launched = Column(Boolean, default=False)  # 礼物是送出去


    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_count(cls, isbn_list):
        # 根据传入一组isbn,, 到Gift表中检索出相应的礼物, 并且计算出某个礼物的Wish心愿数量
        # 一个数量吗? 一组数量
        # db.session 可以做查询, 删除, 添加,
        # filter 需要接收条件表达式
        # mysql in查询
        # isbn wish的数量
        # func.count() 统计数量

        # return count_list[0][1]
        # 对象
        #
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False, Wish.isbn.in_(isbn_list), Wish.status == 1).group_by(Wish.isbn).all()  # filter比filter_by更灵活更加的强大
        count_list = [{'count':w[0], 'isbn':w[1]} for w in count_list]
        return count_list


    @property        # 方法转换成属性
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物, 具体
    # 类代表礼物这个事物, 它是抽象的, 不是具体中的一个
    @classmethod
    def recent(cls):
        # 链式调用
        # 主体, query对象
        # 子函数
        # 触发语句first()  all()
        # limit() 设置显示多少条数据   order_by() 排序  distinct() 去重,要结合group_by()使用  desc() 用来排序
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift


