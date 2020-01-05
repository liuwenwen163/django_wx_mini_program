# encoding: utf-8
import logging
import datetime
import logging
import os
import smtplib
from email.mime.text import MIMEText

from backend import settings

__author__ = "bbw"

logger = logging.getLogger('django')


def demo():
    message = 'Job log in crontab, now time is: ' + str(datetime.datetime.now())
    print(message)
    logger.info(message)


# 分析日志的任务
def statistics():
    # 读取统计log的内容
    data_file = os.path.join(settings.BASE_DIR, 'log', 'statistics.log')
    if not os.path.exists(data_file):
        logger.warning("file not exists. file=[%s]" % data_file)
        return

    result = {}
    with open(data_file, 'r') as data_file:
        for line in data_file:
            line = line.strip()
            content = line.split(' ')[2]
            content_list = content.split(settings.STATISTICS_SPLIT_FLAG)
            # 取出中间件中打印的内容
            log_time = int(content_list[0].split('=')[1][1:-1])
            path = content_list[1].split('=')[1][1: -1]
            full_path = content_list[2].split('=')[1][1:-1]
            cost = float(content_list[3].split('=')[1][1:-1])

            # 记录数据
            # path: value_list
            if path not in result.keys():
                result[path] = []
            result[path].append(cost)  # 每一个请求及请求花费的时间都记录到字典中了

    # 分析数据的最大值、最小值、平均值
    report_content = []
    for k, v_list in result.items():
        # 统计请求次数
        count = len(v_list)
        # 最大值
        v_max = max(v_list)
        # 最小值
        v_min = min(v_list)
        # 平均值
        v_avg = sum(v_list) * 1.00 / count  # 1.00是为了使之变为浮点数
        content = '%-40s    ' \
                  'COUNT: %d    ' \
                  'MAX_TIME: %.4f(s)    ' \
                  'MIN_TIME:%.4f(s)    ' \
                  'AVG_TIME: %.4f(s)' \
                  % (k, count, v_max, v_min, v_avg)
        report_content.append(content)
    return report_content

def report_by_mail():
    logger.info('Begin statistics.')
    content = statistics()
    content = '\r\n'.join(content)
    logger.info('End statistics data.')
    receivers = ['bowen513s@163.com']
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['FROM'] = '[Django Backend]'
    msg['Subject'] = '[Django Service Performance Monitor]'
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()
    logger.info('Send monitor Email success.')



