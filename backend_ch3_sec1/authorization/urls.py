# encoding: utf-8
from django.urls import path

from .views import Test_Session, Test_Session2, \
    UserView, authorize, logout, get_stuatus

__author__ = "bbw"


urlpatterns = [
    path('test', Test_Session.as_view()),
    path('test2', Test_Session2.as_view()),
    path('user', UserView.as_view()),
    path('authorize', authorize),
    path('logout', logout),
    path('status', get_stuatus)
]
