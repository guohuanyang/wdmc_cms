from django.db import models
from datetime import datetime


# Create your models here.
class CurtainCat(models.Model):
    """
    百叶类型
    """
    name = models.CharField(max_length=56, unique=True, verbose_name='类型名称')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '类型管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class CtrDirection(models.Model):
    """
    百叶操控器方向表
    """
    direction = models.CharField(max_length=56, unique=True, verbose_name='操控器位置')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '操控器位置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.direction

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class Color(models.Model):
    """
    颜色管理表
    """
    color = models.CharField(max_length=56, unique=True, verbose_name='帘片颜色')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '颜色信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.color

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class GlassesCat(models.Model):
    """
    玻璃类型
    """
    name = models.CharField(max_length=56, unique=True, verbose_name='类型名称')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '玻璃类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)
