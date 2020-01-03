# encoding: utf-8
"""
展示缓存使用的demo
"""
import os
import time

import django

from django.core.cache import cache

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


def basic_use():
    s = 'Hello World, Hello Django Cache.'
    cache.set('key', s)  # 将字符串放到缓存中，标记是key
    cache_result = cache.get('key')
    print(cache_result)
    # 设置超时时间
    s2 = 'Hello World, Hello Django Timeout Cache.'
    cache.set('key2', s2, 5)
    cache_result = cache.get('key2')
    print(cache_result)
    time.sleep(5)
    cache_result = cache.get('key2')  # 需要重新再取一次
    print(cache_result)

if __name__ == '__main__':
    basic_use()

