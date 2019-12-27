# encoding: utf-8
import json
import os
import random

from django.http import JsonResponse

from backend import settings
from thirdparty import juhe
from utils.response import CommonResponseMixin, ReturnCode

__author__ = "bbw"


constellations = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座','处女座', '天秤座', '天蝎座', '射手座', '摩羯座','水瓶座', '双鱼座']

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
    for stock in popular_stocks:
        result = juhe.stock(stock['market'], stock['code'])
        data.append(result)
        response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)


def constellation(request):
    data = []
    for c in constellations:
        result = juhe.constellation(c)
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
