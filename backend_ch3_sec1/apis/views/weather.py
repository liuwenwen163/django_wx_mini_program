# encoding: utf-8
import json

from django.http import HttpResponse, JsonResponse, FileResponse
from django.views import View

from authorization.models import User
from backend import settings
from thirdparty import juhe
from thirdparty.weather.common import WeatherAPIProxy
from utils.response import CommonResponseMixin, ReturnCode
from utils.auth import already_authorized

__author__ = "bbw"


class WeatherView(View, CommonResponseMixin):
    def get(self, request):
        """根据用户存储的信息查询"""
        if not already_authorized(request):
            response = self.wrap_json_response({}, code=ReturnCode.UNAUTHORIZED)
        else:
            data = []
            open_id = request.session.get('open_id')
            user = User.objects.filter(open_id=open_id)[0]
            cities = json.loads(user.focus_cities)
            for city in cities:
                # result = juhe.weather(city.get('city'))
                result = WeatherAPIProxy.ha_request(city.get('city'),
                                                    timeout=settings.HA_TIMEOUT)
                result['city_info'] = city
                data.append(result)
            response = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
        return JsonResponse(data=response, safe=False)

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







