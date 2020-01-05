# encoding: utf-8
import time
import logging

__author__ = "bbw"

from backend import settings

logger = logging.getLogger('statistics')  # 获取日志实例


# 实现统计时间的中间件
class StatisticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logger.info('Build StatisticsMiddleware.')

    def __call__(self, request):
        tick = time.time()
        response = self.get_response(request)
        path = request.path
        full_path = request.get_full_path()
        tock = time.time()
        cost = tock - tick  # 两个时间相减，获得response处理的时间
        content_list = []
        content_list.append('now=[%d]' % tock)
        content_list.append('path=[%s]' % path)
        content_list.append('full_path=[%s]' % full_path)
        content_list.append('cost=[%.6f]' % cost)
        content = settings.STATISTICS_SPLIT_FLAG.join(content_list)  # 将内容列表变为字符串
        logger.info(content)  # 将统计结果保存进日志中

        return response



