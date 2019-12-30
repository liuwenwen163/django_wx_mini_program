# encoding: utf-8
import json

from django.http import JsonResponse
from django.views import View

from authorization.models import User
from utils.auth import c2s, already_authorized
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
    """关注的城市、股票和星座"""
    def get(self, request):
        """获取用户的数据"""
        if not already_authorized(request):
            # 用户如果未登录，直接返回
            response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
            return JsonResponse(response, safe=False)

        open_id = request.session.get('open_id')  # 如果用户已登录，就可以获取其openid
        user = User.objects.get(open_id=open_id)  # 根据open_id查找出用户
        data = {}
        data['open_id'] = user.open_id
        data['focus'] = {}
        data['focus']['city'] = json.loads(user.focus_cities)  # json字符串需要用json.loads取出数据
        data['focus']['stock'] = json.loads(user.focus_stocks)
        data['focus']['constellation'] = json.loads(user.focus_constellations)
        print('data:', data)

        # 返回用户查询的城市，星座，股票信息
        response = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
        return JsonResponse(response, safe=False)

    def post(self, request):
        """修改用户的数据"""
        # 获取用户
        if not already_authorized(request):
            response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
            return JsonResponse(response, safe=False)
        open_id = request.session.get('open_id')
        user = User.objects.get(open_id=open_id )

        # 将取出的json字符串类型数据保存为字典
        received_body = request.body.decode('utf-8')
        received_body = eval(received_body)

        # 获取数据，
        cities = received_body.get('city')
        stocks = received_body.get('stock')
        constellations = received_body.get('constellation')
        if cities == None: cities = []
        if stocks == None: stocks = []
        if constellations == None: constellations = []

        # 修改数据，保存数据也要保存成json字符串
        user.focus_cities = json.dumps(cities)
        user.focus_stocks = json.dumps(stocks)
        user.focus_constellations = json.dumps(constellations)
        user.save()

        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message='修改用户信息成功.')
        return JsonResponse(response, safe=False)


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
