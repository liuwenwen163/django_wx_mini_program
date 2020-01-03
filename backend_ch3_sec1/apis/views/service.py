# encoding: utf-8
import json
import os
import random
import logging

from django.core.cache import cache
from django.http import JsonResponse

from backend import settings
from thirdparty import juhe
from utils import timeutil
from utils.auth import already_authorized, get_user
from utils.response import CommonResponseMixin, ReturnCode

__author__ = "bbw"

logger = logging.getLogger('django')

all_constellations = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座','处女座', '天秤座', '天蝎座', '射手座', '摩羯座','水瓶座', '双鱼座']

popular_stocks = [
    {
        'code': '000001',
        'name': '平安银行',
        'market': 'sz'
    },
    {
        'code': '000002',
        'name': '万科A',
        'market': 'sz'
    },
    {
        'code': '600036',
        'name': '招商银行',
        'market': 'sh'
    },
    {
        'code': '601398',
        'name': '工商银行',
        'market': 'sh'
    }
]

all_jokes = []


def stock(request):
    data = []
    stocks = []
    # 如果登录就显示登录用户关注的股票，否则显示预定义的股票
    if already_authorized(request):
        user = get_user(request)
        stocks = json.loads(user.focus_constellations)
    else:
        stocks = popular_stocks
    for stock in popular_stocks:
        result = juhe.stock(stock['market'], stock['code'])
        data.append(result)
        response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)


# 星座运势
def constellation(request):
    data = []
    # 用户已登录的话，就显示登录用户关注的星座运势，否则就返回所有星座的运势
    if already_authorized(request):
        user = get_user(request)  # get_user根据request中的session获取用户对象
        constellations = json.loads(user.focus_constellations)
    else:
        constellations = all_constellations
    for c in constellations:
        result = cache.get(c)
        if not result:
            result = juhe.constellation(c)
            timeout = timeutil.get_day_left_in_second()  # 计算当天剩余时间，秒为单位
            cache.set(c, result, timeout)
            logger.info("set cache. key=[%s], value=[%s], timeout=[%d]" %(c, result, timeout))

        data.append(result)
    response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)

def joke(request):
    global all_jokes
    # 判断下缓存中有无这个变量，避免每次都要读取
    if not all_jokes:
        all_jokes = json.load(open(os.path.join(settings.BASE_DIR, 'jokes.json'), 'r'))
    limits = 10
    sample_jokes = random.sample(all_jokes, limits)
    response = CommonResponseMixin.wrap_json_response(data=sample_jokes)
    return JsonResponse(data=response, safe=False)
