# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# Python多线程到底是不是鸡肋
# GIL node.js 单进程  单线程
# 10 线程  非常严重的依赖CPU的计算  CPU密集型程序

# IO密集型的程序   查询数据库, http请求, 请求网络资源, 读写额贩卖

# io 密集型程序 主要时间用在等待

# flask web框架
# 请求  线程
# 10个请求  flask开启多少个线程来处理请求
# webserver
# Java  PHP  nginx  Apache  Tomcat IIS