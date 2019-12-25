# encoding: utf-8
import json

from django.http import HttpResponse, JsonResponse, FileResponse
from django.views import View

from thirdparty import juhe
from utils.response import CommonResponseMixin

__author__ = "bbw"


class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        """使用post来响应天气查询，在body中填写城市信息更加容易"""
        data = []
        received_body = request.body.decode('utf-8')  # 获取body中的数据
        received_body = json.loads(received_body)  # 使用json标准库加载数据
        cities = received_body.get('cities')  # 获取post过来的信息data数据
        for city in cities:
            result = juhe.weather(city.get('city'))
            result['city_info'] = city
            data.append(result)
        data = self.wrap_json_response(data=data)  # 从Mixin继承来的方法
        return JsonResponse(data=data, safe=False)







