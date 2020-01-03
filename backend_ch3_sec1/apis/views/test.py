# encoding: utf-8
from django.http import HttpResponse

__author__ = "bbw"

def test(request):
    return HttpResponse('Hello World')
