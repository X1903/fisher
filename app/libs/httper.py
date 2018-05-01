# _*_ coding:utf-8 _*_
__author__ = 'Xbc'


import json
from urllib import request

import requests


# ﻿http://t.yushu.im/v2/book/isbn/9787501524044

class HTTP(object):
    # 经典了和新式类

    @staticmethod
    def get(url, return_json=True):
        """
        get 获取数据
        :param url: <str>:获取地址
        :param return_json: <bool>:是否返回json格式的数据
        :return: <dict> or str
        """

        # restful
        # json

        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # if r.status_code == 200:
        #
        #     # 判断是否要json数据,,否则返回text
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''