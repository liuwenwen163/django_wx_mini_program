# encoding: utf-8
from django.urls import path

from .views import Test_Session, Test_Session2

__author__ = "bbw"


urlpatterns = [
    path('test', Test_Session.as_view()),
    path('test2', Test_Session2.as_view())
]
