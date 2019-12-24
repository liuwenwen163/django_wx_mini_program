# encoding: utf-8
from django.urls import path

from .views import weather

__author__ = "bbw"

urlpatterns = [
    path('', weather.weather),
]
