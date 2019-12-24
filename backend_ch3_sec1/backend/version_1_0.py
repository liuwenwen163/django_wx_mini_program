# encoding: utf-8

__author__ = "bbw"

from django.urls import path,include

urlpatterns = [
    path('service/', include('apis.urls'))
]
