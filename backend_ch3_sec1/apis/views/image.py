# encoding: utf-8
import os
from django.http import Http404, HttpResponse, FileResponse, JsonResponse

from backend import settings
import utils.response

__author__ = "bbw"


def image(request):
    """获取并返回图片的"""
    if request.method == 'GET':
        # MD5是作为url的参数传入进来的
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return Http404()
        else:
            """方法一：使用HttpResponse
            #这里获取的data是二进制流，直接返回客户端会乱码
            # data = open(imgfile, 'rb').read()  # imgfile是文件路径
            # 告诉客户端data的类型是图片
            # return HttpResponse(content=data, content_type='image/jpg')"""
            #  方法二：使用FileResponse一步到位
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')


def image_text(request):
    """获取图片，并添加上附加信息，作为Json数据返回给客户端"""
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return utils.response.wrap_json_response(
                code=utils.response.ReturnCode.RESOURCES_NOT_EXISTS
            )
        else:
            response_data = {}
            response_data['name'] = md5 + '.jpg'
            response_data['url'] = '/service/image?md5=%s' % (md5)
            response = utils.response.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe=False)

