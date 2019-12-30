from django.db import models

# Create your models here.

class User(models.Model):
    open_id = models.CharField(max_length=32, unique=True)
    nickname = models.CharField(max_length=256)  # 昵称
    focus_cities = models.TextField(default='[]')  # 关注的城市
    focus_constellations = models.TextField(default='[]')  # 关注的星座
    focus_stocks = models.TextField(default='[]')  # 关注的股票
