# encoding: utf-8
import logging
import datetime
import logging

__author__ = "bbw"

logger = logging.getLogger('django')


def demo():
    message = 'Job log in crontab, now time is: ' + str(datetime.datetime.now())
    print(message)
    logger.info(message)
