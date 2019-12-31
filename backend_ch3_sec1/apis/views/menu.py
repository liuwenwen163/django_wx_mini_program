# encoding: utf-8
"""
    加载应用配置，并且返回前台
"""
import json
import os
import yaml
from django.http import JsonResponse
from django.views import View

from apis.models import App
from authorization.models import User
from backend import settings
from utils.auth import already_authorized, get_user
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
        query_set = App.objects.all()
        all_app = []
        for app in query_set:
            all_app.append(app.to_dict())
        print(all_app)
        response = self.wrap_json_response(data=all_app)
        print(response)
        return JsonResponse(data=response, safe=False)


class UserMenu(View, CommonResponseMixin):
    def get(self, request):
        # 如果未登录，返回未鉴权
        if not already_authorized(request):
            response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
            return JsonResponse(response, safe=False)
        # 否则返回用户定制的menu
        open_id = request.session.get('open_id')
        user = User.objects.get(open_id=open_id)
        # 利用了多对多关系，获取用户对应的全部应用列表
        menu_list = user.menu.all()

        user_menu = []
        for app in menu_list:
            user_menu.append(app.to_dict())
        response = self.wrap_json_response(data=user_menu, code=ReturnCode.SUCCESS)
        return JsonResponse(response, safe=False)

    def post(self, request):
        # 如果未登录，返回未鉴权
        if not already_authorized(request):
            response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
            return JsonResponse(response, safe=False)
        user = get_user(request)
        post_menu = json.loads(request.body.decode('utf-8'))
        post_menu = post_menu.get('data')
        focus_menu = []
        print(post_menu)
        for item in post_menu:
            print(item)
            print(item.get('appid'))
            item = App.objects.get(appid=item.get('appid'))
            print(item)
            focus_menu.append(item)
        print(focus_menu)
        user.menu.set(focus_menu)
        user.save()
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS)
        return JsonResponse(response, safe=False)
