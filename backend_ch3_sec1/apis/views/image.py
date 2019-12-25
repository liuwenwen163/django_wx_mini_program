# encoding: utf-8
import hashlib
import os
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from django.views import View

from backend import settings
from utils.response import ReturnCode, CommonResponseMixin

__author__ = "bbw"


class ImageView(View, CommonResponseMixin):
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
        """将用户上传的图片进行保存"""
        files = request.FILES
        response = []
        for key, value in files.items():  # key是文件名，value是文件对象
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
            with open(path, 'wb') as f:
                f.write(content)
            # 将文件名称和md5告诉给前台
            response.append({
                'name': key,
                'md5': md5
            })
        message = 'post method success.'
        response = self.wrap_json_response(
            data=response,
            code=ReturnCode.SUCCESS,
            message=message
        )
        return JsonResponse(data=response, safe=False)

    def put(self, request):
        message = 'put method success.'
        response = self.wrap_json_response(code=ReturnCode.SUCCESS ,message=message)
        return JsonResponse(data=response, safe=False)

    def delete(self, request):
        md5 = request.GET.get('md5')
        img_name = md5 + '.jpg'
        path = os.path.join(settings.IMAGES_DIR, img_name)
        if os.path.exists(path):
            os.remove(path)
            message = 'Remove success.'
        else:
            message = 'file(%s) not found' % img_name

        response = self.wrap_json_response(code=ReturnCode.SUCCESS ,message=message)
        return JsonResponse(data=response, safe=False)


# def image_text(request):
#     """获取图片，并添加上附加信息，作为Json数据返回给客户端"""
#     if request.method == 'GET':
#         md5 = request.GET.get('md5')
#         imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
#         if not os.path.exists(imgfile):
#             return response.wrap_json_response(
#                 code=utils.response.ReturnCode.RESOURCES_NOT_EXISTS
#             )
#         else:
#             response_data = {}
#             response_data['name'] = md5 + '.jpg'
#             response_data['url'] = '/service/image?md5=%s' % (md5)
#             response = utils.response.wrap_json_response(data=response_data)
#             return JsonResponse(data=response, safe=False)

