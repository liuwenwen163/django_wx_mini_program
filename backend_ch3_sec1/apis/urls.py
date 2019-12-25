# encoding: utf-8
from django.urls import path

from .views import menu
from .views.weather import WeatherView
from .views.image import ImageView
from .views.menu import GetMenu

__author__ = "bbw"

urlpatterns = [
    # 在应用中将url路由到具体的视图中
    path('weather', WeatherView.as_view()),
    path('menu', GetMenu.as_view()),
    path('image', ImageView.as_view()),
    # path('imagetext', image.image_text)
]
