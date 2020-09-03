from categorys.models import GlassesCat, CurtainCat, CtrDirection, Color
from django.db import models
from _datetime import datetime
# Create your models here.


class Area(models.Model):
    """
    本次计算平方大小
    """
    width = models.IntegerField(verbose_name='尺寸宽(mm)', default=0)
    height = models.IntegerField(verbose_name='尺寸高(mm)', default=0)
    square = models.FloatField(verbose_name='平方数(㎡)', default=0.0)
    real_square = models.FloatField(verbose_name='实际平方数(㎡)', default=0.0)
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '平方信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.real_square)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.square == 0.0:
            # 自动计算平方数
            self.square = round(self.width * self.height / 1000000 + 0.0000001, 2)
        if self.real_square == 0.0:
            self.real_square = self.square
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class Curtain(models.Model):
    """
    百叶信息表
    """
    min_square_choices = (
        ('0.0', '0.0'),
        ('0.3', '0.3'),
        ('0.35', '0.35'),
        ('0.4', '0.4'),
        ('0.45', '0.45'),
        ('0.5', '0.5'),
        ('0.6', '0.6'),
        ('0.7', '0.7'),
        ('1', '1'),
    )
    sub_cat = models.ForeignKey(CurtainCat, on_delete=models.CASCADE, verbose_name='百叶类型')
    name = models.CharField(max_length=256, null=True, blank=True, verbose_name='百叶名称')
    color = models.ForeignKey(Color, on_delete=models.CASCADE,
                              null=True, blank=True, verbose_name='帘片颜色')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='面积大小', null=True, blank=True)
    price = models.FloatField(verbose_name='单价', default=400.0)
    min_square = models.CharField(max_length=20, default='0.0', choices=min_square_choices, verbose_name='起算平方')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '百叶信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class IndoorGlasses(models.Model):
    """
    室内玻璃管理
    """
    sub_cat = models.ForeignKey(GlassesCat, on_delete=models.CASCADE, verbose_name='玻璃类型')
    name = models.CharField(max_length=256, verbose_name='玻璃名称')
    label = models.CharField(max_length=40, verbose_name='玻璃标签备注', null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='面积大小', null=True, blank=True)
    price = models.FloatField(verbose_name='单价', default=30.0)
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '室内玻璃信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class OutdoorGlasses(models.Model):
    """
    室外玻璃管理
    """

    sub_cat = models.ForeignKey(GlassesCat, on_delete=models.CASCADE, verbose_name='玻璃类型')
    name = models.CharField(max_length=256, verbose_name='玻璃名称')
    label = models.CharField(max_length=40, verbose_name='玻璃标签备注', null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='面积大小', null=True, blank=True)
    price = models.FloatField(verbose_name='单价', default=60.0)
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '室外玻璃信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)
