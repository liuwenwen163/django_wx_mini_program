# encoding: utf-8
import os
import django
import logging

__author__ = "bbw"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


def logdemo():
    # 括号中的参数，是settings中logger配置的key
    logger = logging.getLogger('django')
    logger.info('hello logging')  # 打印一行日志查看


if __name__ == '__main__':
    logdemo()
