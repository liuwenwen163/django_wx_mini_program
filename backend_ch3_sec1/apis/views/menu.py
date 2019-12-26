# encoding: utf-8
"""
    加载应用配置，并且返回前台
"""
import os
import yaml
from django.http import JsonResponse
from django.views import View

from backend import settings
from utils.response import CommonResponseMixin, ReturnCode

__author__ = "bbw"


def init_app_data():
    """该函数是用来初始化注册应用的"""
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        # yaml是用来配置项目应用的，当项目应用做成了可拓展的形式，就可以用app.yaml进行拓展
        apps = yaml.load(f)
        return apps


class GetMenu(View, CommonResponseMixin):
    def get(self, request):
        # 获取到的是init_app返回的全部的应用信息
        global_app_data = init_app_data()
        published_app_data = global_app_data.get('published')  # 获取已经发布的应用信息
        # 将数据返回之前，做一些额外的封装，加上状态码
        response = self.wrap_json_response(
            data=published_app_data,
            code=ReturnCode.SUCCESS
        )
        # 这里返回的数据就是前端menu显示的菜单
        return JsonResponse(data=response, safe=False,)
