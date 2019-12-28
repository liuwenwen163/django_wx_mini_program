# encoding: utf-8
import json

from django.http import JsonResponse
from django.views import View

from authorization.models import User
from utils.auth import c2s
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


class UserView(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        pass


def __authorize_by_code(request):
    """
    使用wx.login拿到的临时code到微信提供的code2session接口授权
    """
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    code = post_data.get('code').strip()
    app_id = post_data.get('appId').strip()
    nickname = post_data.get('nickname').strip()

    response = {}
    if not code or not app_id:
        response['message'] = '认证不完整，需要完整数据'
        response['code'] = ReturnCode.BROKEN_AUTHORIZED_DATA
        return JsonResponse(data=response, safe=False)

    # 将app_id和code拼凑成url，去微信接口服务做认证，返回值是认证结果
    data = c2s(app_id, code)
    openid = data.get('openid')
    print('get openid:',openid)
    if not openid:
        # 如果openid不存在，返回认证失败的接口信息
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message='auth failed')
        return JsonResponse(data=response, safe=False)

    # open_id存在就做进一步开发，利用session中间件标记两个数据
    request.session['open_id'] = openid
    request.session['is_authorized'] = True

    if not User.objects.filter(open_id=openid):
        # 如果数据库中查不到这个open_id就保存
        new_user = User(open_id=openid, nickname=nickname)
        print('new user: open_id: %s, nickname: %s' %(openid, nickname))
        new_user.save()

    response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message='auth success')
    return JsonResponse(data=response, safe=False)


def authorize(request):
    return __authorize_by_code(request)
