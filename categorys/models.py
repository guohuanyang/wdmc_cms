from django.db import models
from datetime import datetime


# Create your models here.
class CurtainCat(models.Model):
    """
    百叶类型
    """
    name = models.CharField(max_length=56, unique=True, verbose_name='类型名称')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '类型管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Color(models.Model):
    """
    颜色管理表
    """
    color = models.CharField(max_length=56, unique=True, verbose_name='帘片颜色')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '颜色信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.color
