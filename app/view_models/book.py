# _*_ coding:utf-8 _*_
__author__ = 'Xbc'


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = book['author']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [str(self.author), str(self.publisher), str(self.price)])
        print(type(intros))
        return ' / '.join(intros)


class BookCollection:

    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
    # 描述特征 (类变量, 实例变量)
    # 行为 (方法)
    # 面向过程
    # 统一结构

    @classmethod
    def pacage_single(cls, data, keyword):
        '''处理单本书的数据'''
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned


    @classmethod
    def __cut_book_data(cls, data):

        book = {
            'title':data['title'],
            'publisher':data['publisher'],
            'pages':data['pages'] or '',
            'author':','.join(data['author']),  # 把老师列表变成字符串
            'price':data['price'],
            'summary':data['summary'] or '',
            'image':data['image']
        }
        return book
    
    
    @classmethod
    def __cut_books_data(cls, data):
        books = []
        for book in data['books']:
            r = {
                'title': book['title'],
                'publisher': book['publisher'],
                'pages': book['pages'],
                'author': ','.join(book['author']),  # 把老师列表变成字符串
                'price': book['price'],
                'summary': book['summary'],
                'image': book['image']
            }
            books.append(r)
        return books