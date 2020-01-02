# encoding: utf-8
import logging

__author__ = "bbw"


class TestFilter(logging.Filter):
    def filter(self, record):
        """
        :param record:每一条日志具体的内容，类型是类
        return：如果返回值是 True，代表日志会被打印出来；
        如果返回值是 False，代表日志会被过滤掉
        """
        if '----' in record.msg:
            # 如果 '' 内的内容是在record中，那么日志就是没有用的
            return False
        else:
            return True

