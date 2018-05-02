# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

import threading
import time

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

# Python的多线程是鸡肋

t = threading.current_thread()
print(t.getName())

# 主线程