# _*_ coding:utf-8 _*_


__author__ = 'Xbc'


from flask import jsonify, Blueprint, request, render_template, flash
import json

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection
# from . import web


# 蓝图 blueprint  蓝本
# web = Blueprint('web', __name__)
from . import web

@web.route('/book/search')   #http://0.0.0.0:5000/book/search/9787501524044/0
def search():
    '''
        q:    普通的关键字  isbn
        page  页码
        ?q=金庸&page=1
    :return:
    '''

    # Request Response
    # HTTP 的请求信息
    # 查询参数 POST 参数 remote ip

    form = SearchForm(request.args)     # http://0.0.0.0:5000/book/search?q=%E9%83%AD%E6%95%AC%E6%98%8E&page=2    http://0.0.0.0:5000/book/search?q=%E7%BA%A2%E6%A5%BC%E6%A2%A6&page=1
    books = BookCollection()
    if form.validate():
        # q = request.args['q']
        # page = request.args['page']
        # ip = request.remote_addr
        # print(q, page, ip)

        q = form.q.data.strip()         # http://0.0.0.0:5000/book/search?q=9787501524044
        page = form.page.data           # http://0.0.0.0:5000/book/search?q=红楼梦

        # a = request.args.to_dict()  # 把不可变字典变成可变字典

        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.pacage_single(result, q)
        else:
            yushu_book.search_by_keyword(q, page)
            # result = YuShuBook.search_by_keyword(q, page)
            # result = BookViewModel.package_collection(result, q)

        # return json.dumps(result), 200, {'content-type':'application/json'}
        # return jsonify(result)

        # __dict__
        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books.__dict__)
    else:
        flash('搜索的关键字不符合要求, 请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('./search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


# @web.route('/testa')
# def test1():
#     from flask import request
#     from app.libs.none_local import n
#
#     print(n.v)
#     n.v = 2
#     print(n.v)
#     print("----------------")
#     print(getattr(request, 'v', None))
#     setattr(request, 'v', 2)
#     print(request.v)
#     print("*"*100)
#     return  'ok'



# @web.route('/testb')
# def testb():
#     r = {
#         'name':'',
#         'age':18
#     }
#
#     flash('hello, qiyue')
#
#     # return jsonify(r)
#     return render_template('demo_test/testa.html', data=r) # 填充的模板, 填充的数据
#
# @web.route('/test2')
# def test2():
#     r = {
#         'name': '七月',
#         'age': 18
#     }
#     return render_template('demo_test/test2.html', data=r)