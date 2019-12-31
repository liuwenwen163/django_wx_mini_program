# encoding: utf-8
import json
import requests
from utils import proxy
import backend.settings

from authorization.models import User

from utils.wx.crypt import WXBizDataCrypt
from utils.wx.code2session import code2session

__author__ = "bbw"


# 判断是否已经授权
def already_authorized(request):
    is_authorized = False

    if request.session.get('is_authorized'):
        is_authorized = True
    return is_authorized


def get_user(request):
    # 封装了查询session中的open_id，根据open_id查询对应的用户对象
    if not already_authorized(request):
        raise Exception('not authorized request')
    open_id = request.session.get('open_id')
    user = User.objects.get(open_id=open_id)
    return user


def c2s(appid, code):
    return code2session(appid, code)

'''
return data 的格式
{
  "session_key": "JmRNs6uPEpFzlMRmg4NqJQ==",
  "expires_in": 7200,
  "openid": "oXSML0ZH05BItFTFILfgCGxXxxik"
}
'''
def code2session(appid, code):
    """
    将API，params，url拼凑成地址，发送到微信的接口服务
    将结果返回
    """
    API = 'https://api.weixin.qq.com/sns/jscode2session'
    params = 'appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % \
             (appid, backend.settings.WX_APP_SECRET, code)
    url = API + '?' + params
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    print(data)
    return data
