# _*_ coding:utf-8 _*_
__author__ = 'Xbc'




from app.libs.httper import HTTP
from flask import current_app

class YuShuBook(object):

    # 模型层 MVC M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self,isbn):
        '''isbn搜索'''
        url = self.isbn_url.format(isbn)
        # url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_singie(result)
        # dict

        # 时间价值
        # book = query_from_mysql(isbn)
        # if book:
        #   return boook
        # else:
        #   save(reslt)

        # return result

    def __fill_singie(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, page=1):
        '''关键字搜索'''
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)
        # return result

    def calculate_start(self, page):
        '''计算分页数量'''
        return (int(page)-1) * current_app.config['PER_PAGE']
    
    
    
    
