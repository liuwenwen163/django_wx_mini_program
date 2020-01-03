# encoding: utf-8
import datetime


__author__ = "bbw"


def get_day_left_in_second():
    """
    返回一天剩余的时间（单位：秒）
    """
    now = datetime.datetime.now()  # 获取当前时间
    tomorrow = now + datetime.timedelta(days=1)  # 获取第二天时间
    left = (datetime.datetime(tomorrow.year,
                              tomorrow.month,
                              tomorrow.day,
                              0, 0, 0) - now)
    return int(left.total_seconds())


if __name__ == '__main__':
    print(get_day_left_in_second())
