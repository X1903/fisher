# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# 原理  字典  保存数据
# 操作数据
# werzeug  local   字典

# LocalStack  Local 字典
# Local使用字典的方式实现线程隔离
# 线程隔离的站结构
# 封装  如果一次封装解决不了问题, 牛么就再来一次
# 宝成也是一种艺术 含蓄


# {thread_id1:value1,thread_id2:value2...}
# L 线程隔离对象
# t1  L.a  t2 L.a
# Local

import threading
import time

from werkzeug.local import Local  # Local 线程隔离的对象

class A:
    b = 1

# my_obj = A()
my_obj = Local
my_obj.b = 1

def worker():
    # 新进场
    my_obj.b = 2
    print('in new thread b is : ' + str(my_obj.b) )

new_t = threading.Thread(target=worker, name='xbc_thread')
new_t.start()
# time.sleep(1)
# 主线程
print('in main thread b is :' + str(my_obj.b))