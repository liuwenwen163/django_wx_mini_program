# encoding: utf-8
import json

from django.http import HttpResponse, JsonResponse, FileResponse

from thirdparty import juhe

__author__ = "bbw"


def weather(request):
    if request.method == "GET":
        city = request.GET.get('city')
        data = juhe.weather(city)

        return JsonResponse(data=data, status=200)
    elif request.method == 'POST':
        # 获取请求body中的城市信息
        received_body = request.body
        # 使用json进行数据解码
        received_body = json.loads(received_body)
        cities = received_body.get('cities')

        response_data = []
        for city in cities:
            result = juhe.weather(city)
            result['city'] = city
            response_data.append(result)
        return JsonResponse(data=response_data, safe=False, status=200)





