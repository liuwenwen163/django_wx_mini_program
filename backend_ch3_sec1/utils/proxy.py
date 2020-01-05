# encoding: utf-8
import backend.settings

__author__ = "bbw"


def proxy():
    if backend.settings.USE_PROXY:
        # add your proxy here
        return {'http:' 'www.baidu.com'}  # 返回一个错误的代理，模拟请求错误
    else:
        return {}
