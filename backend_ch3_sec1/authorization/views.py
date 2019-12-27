# encoding: utf-8
from django.http import JsonResponse
from django.views import View

from utils.response import CommonResponseMixin, ReturnCode

__author__ = "bbw"


class Test_Session(View, CommonResponseMixin):
    def get(self, request):
        # 如果开启了session，request就多了一个session属性,并操作该属性
        request.session['message'] = 'Test Django Session OK'
        response = self.wrap_json_response(code=ReturnCode.SUCCESS)
        return JsonResponse(data=response, safe=False)


class Test_Session2(View, CommonResponseMixin):
    """测试用户是否是真的可以拿到session"""
    def get(self, request):
        print('session content:', request.session.items())
        response = self.wrap_json_response(code=ReturnCode.SUCCESS)
        return JsonResponse(data=response, safe=False)


