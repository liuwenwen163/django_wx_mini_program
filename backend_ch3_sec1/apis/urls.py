# encoding: utf-8
from django.urls import path

from .views import weather, menu, image

__author__ = "bbw"

urlpatterns = [
    # 在应用中将url路由到具体的视图中
    path('weather', weather.weather),
    path('menu', menu.get_menu),
    path('image', image.image),
    path('imagetext', image.image_text)
]
