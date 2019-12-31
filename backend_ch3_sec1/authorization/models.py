from django.db import models

# Create your models here.
from apis.models import App


class User(models.Model):
    open_id = models.CharField(max_length=32, unique=True)
    nickname = models.CharField(max_length=256)  # 昵称
    focus_cities = models.TextField(default='[]')  # 关注的城市
    focus_constellations = models.TextField(default='[]')  # 关注的星座
    focus_stocks = models.TextField(default='[]')  # 关注的股票

    # 用户表和应用表实现多对多的关系映射
    menu = models.ManyToManyField(App)

    class Meta:
        indexes = [
            # 数组的每一项就是一个索引
            # models.Index(fields=['nickname']),
            models.Index(fields=['open_id', 'nickname'])
        ]

