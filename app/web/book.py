# _*_ coding:utf-8 _*_


__author__ = 'Xbc'


from flask import jsonify, Blueprint, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
# from . import web


# 蓝图 blueprint
web = Blueprint('web', __name__)

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

    form = SearchForm(request.args)
    if form.validate():
        q = request.args['q']
        page = request.args['page']
        print(q, page)

        # a = request.args.to_dict()  # 把不可变字典变成可变字典

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)


        # return json.dumps(result), 200, {'content-type':'application/json'}
        return jsonify(result)
    else:
        return jsonify(form.errors)