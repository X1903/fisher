# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import threading
import time

# 字典
# PHP 数组
# request = {'key1:value2, key2:value2...}
# 多线程  唯一标致
# request = {'thread_key1:value2, thread_key2:value2...}
# ID号
# 线程隔离


def worker():
    print('i an thread')
    t = threading.current_thread()
    time.sleep(2)
    print(t.getName())

new_t = threading.Thread(target=worker, name='xbc_thread')
new_t.start()

# 更加充分利用CPU的性能优势
# 异步进程
# 单核的CPU
# 4核 A核 B核  并行的执行程序
# Python 不能充分利用多核CPU优势

# Python的多线程是鸡肋   # 食之无味 弃之可惜

# GTL 全局解释锁  global  interpreter  lock
# 锁  线程安全

# 进程管理内存资源  一个进程  多个线程  共享
# 线程不安全

# a = 3

# A a+=1
# print(a)

# B a+=1
# print(a)

# 锁
# 细粒度锁 程序员  主动加锁
# 粗粒度锁  解释器  GIL 多核CPU 1个线程执行  一定程度上保证线程安全
# a+=1
# bytecode
# python cpython jpython
# 多进程  进程间通信技术

t = threading.current_thread()
print(t.getName())

# 主线程