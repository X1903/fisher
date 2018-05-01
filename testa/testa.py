# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

from flask import Flask, current_app, request

app = Flask(__name__)

# 应用上下文Flask
# 请求上下文request

# Flask AppContext
# Request RequestContext
# 离线应用, 单元测试

# ctx = app.app_context()
# ctx.push()  # 返回的是核心对象APP    入栈的方法
#
# a = current_app
# d = current_app.config['DEBUG']   # RuntimeError: Working outside of application context.
#
# ctx.pop()


# 只要一个类实现了__enter__  和 __exit__ 方法就可以使用with语句
# 实现了上下文协议的对象使用with
# 上下文管理器

with app.app_context():   # 上下文表达式
    a = current_app
    d = current_app.config['DEBUG']

# 1. l连接数据库      写到上下文管理器__enter__里面
# 2. sql 逻辑代码    写到with语句的代码块里面
# 3. 释放资源         写到__exit__ 里面

try:
    pass
except Exception:
    pass
finally:
    pass


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):   # 回收资源,,处理异常
        if exc_tb:
            print("处理异常")
        else:
            print("no exception")
        print('close resource connection')

        # return True  # 外部不会发生异常
        return False   # 外部会发生异常,, 默认返回False

    def query(self):
        print('query data')

try:
    with MyResource() as resource:
        resource.query()
except Exception as ex:
    pass
