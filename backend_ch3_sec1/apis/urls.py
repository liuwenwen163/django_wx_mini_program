# encoding: utf-8
from django.urls import path

from .views import menu
from .views.weather import WeatherView
from .views.image import ImageView, ImageListView
from .views.menu import GetMenu, UserMenu
from .views.service import stock, constellation, joke
from .views.test import test

__author__ = "bbw"

urlpatterns = [
    # 在应用中将url路由到具体的视图中
    path('weather', WeatherView.as_view()),
    # path('menu', GetMenu.as_view()),
    path('menu/list', GetMenu.as_view()),
    path('menu/user', UserMenu.as_view()),
    path('image', ImageView.as_view()),
    path('image/list', ImageListView.as_view()),
    path('stock', stock),
    path('constellation', constellation),
    path('joke', joke),
    path('test', test)
]
