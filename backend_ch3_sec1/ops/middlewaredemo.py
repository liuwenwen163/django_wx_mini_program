# encoding: utf-8
import logging

__author__ = "bbw"

logger = logging.getLogger('django')


class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # 初始化这个类的时候，打印日志
        logger.info("Build TestMiddleware")

    def __call__(self, request):
        logger.info("TestMiddleware before request.")  # 请求前打印log
        response = self.get_response(request)  # 处理请求
        logger.info('TestMiddleware after request.')  # 请求后打印log
        return response

