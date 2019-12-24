# encoding: utf-8
from django.http import HttpResponse, JsonResponse, FileResponse


__author__ = "bbw"


# def helloworld(request):
#
#     print('request method', request.method)
#     print('request META:', request.META)
#     print('request cookies:', request.COOKIES)
#
#     return HttpResponse(content='ok', status=201)
#
#
def helloworld(request):
    m = {
        "message": "Hello Django"
    }
    # safe为false会默认将任何python对象转换为json
    return JsonResponse(data=m, safe=False, status=200)


def helloworld(request):
    # 默认情况下，content可以省略
    return HttpResponse(content='ok', status=201)


