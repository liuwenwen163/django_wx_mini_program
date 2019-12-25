# encoding: utf-8
import os
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from django.views import View

from backend import settings
import utils.response

__author__ = "bbw"


class ImageView(View, utils.response.CommonResponseMixin):
    """
    utils.response.CommonResponseMixin是Mixin多继承
    通过Mixin可以直接使用self来调用额外扩展的方法wrap_json_response
    """
    def get(self, request):
        # MD5是作为url的参数传入进来的
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return Http404()
        else:
            #  使用FileResponse一步到位,直接渲染的是文件
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')

    def post(self, request):
        message = 'post method success.'
        # 通过使用Mixin，可以直接调用通过Mixin定义的函数了
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)

    def put(self, request):
        message = 'put method success.'
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)

    def delete(self, request):
        message = 'delete method success.'
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)


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

