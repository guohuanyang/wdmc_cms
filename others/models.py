from django.db import models
from datetime import datetime


class Customer(models.Model):
    """
    顾客管理表
    """
    gender_choice = (
        ("男", "男"),
        ("女", "女"),
    )
    name = models.CharField(max_length=256, verbose_name='名称')
    gender = models.CharField(max_length=10, choices=gender_choice, default='男', verbose_name='性别')
    phone = models.CharField(max_length=40, verbose_name='电话号码')
    goods_address = models.CharField(max_length=256, verbose_name='送货地址')
    house_address = models.CharField(max_length=256, verbose_name='住宅地址', null=True, blank=True)
    other_link = models.CharField(max_length=40, null=True, blank=True, verbose_name='其他联系方式')
    is_important = models.BooleanField(default=False, verbose_name='是否是重要客户')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '顾客信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class GlassesFactory(models.Model):
    """
    钢化厂表
    """
    fac_name = models.CharField(max_length=30, verbose_name='钢化厂名称')
    name = models.CharField(max_length=30, verbose_name='联系人名称', null=True, blank=True)
    address = models.CharField(max_length=30, verbose_name='钢化厂地址', null=True, blank=True)
    phone = models.CharField(max_length=40, verbose_name='联系方式')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '钢化厂信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.fac_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)
