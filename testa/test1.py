# _*_ coding:utf-8 _*_
__author__ = 'Xbc'


import  random


def generate_app(num):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed))

    salt = ''.join(sa)
    print(salt)


generate_app(10)

