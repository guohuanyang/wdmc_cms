# Create your models here.
from goods.models import Curtain, IndoorGlasses, OutdoorGlasses
from others.models import Customer, GlassesFactory
from categorys.models import GlassesCat, CurtainCat, CtrDirection
from django.db import models
from datetime import datetime


class GlassOrder(models.Model):
    """
    玻璃订单表
    """
    status_choices = (
        ("已下单", "已下单"),
        ("已收货", "已收货"),
        ("已发货", "已发货"),
        ("已完成", "已完成"),
    )
    tr_code = models.CharField(max_length=56, unique=True, verbose_name='玻璃订单号', null=True, blank=True)
    indoor_glasses = models.ForeignKey(IndoorGlasses, on_delete=models.CASCADE, verbose_name='室内玻璃编号')
    indoor_num = models.IntegerField(default=1, verbose_name='室内玻璃数量')
    indoor_real_square = models.FloatField(default=0.0, verbose_name='室内玻璃实际平方数')
    indoor_total_price = models.FloatField(default=0.0, verbose_name='室内玻璃总价')
    outdoor_glasses = models.ForeignKey(OutdoorGlasses, on_delete=models.CASCADE, verbose_name='室外玻璃编号')
    outdoor_num = models.IntegerField(default=1, verbose_name='室外玻璃数量')
    outdoor_real_square = models.FloatField(default=0.0, verbose_name='室外玻璃实际平方数')
    outdoor_total_price = models.FloatField(default=0.0, verbose_name='室外玻璃总价')
    real_total_square = models.FloatField(default=0.0, verbose_name='实际总平方数(室内+室外)')
    total_price = models.FloatField(default=0.0, verbose_name='玻璃订单总价')
    money_remark = models.CharField(max_length=256, verbose_name='订单备注', null=True, blank=True)
    real_total_price = models.FloatField(default=0.0, verbose_name='玻璃订单实际总价')
    glasses_order_status = models.CharField(max_length=56, verbose_name='玻璃订单状态', choices=status_choices, default='已下单')
    plan_time = models.DateTimeField(default=datetime.now, verbose_name='玻璃要求到货时间')
    reach_time = models.DateTimeField(default=datetime.now, verbose_name='玻璃实际到货时间')
    pay_time = models.DateTimeField(default=datetime.now, verbose_name='玻璃下单时间')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '玻璃订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tr_code

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.tr_code = self.create_at.strftime('%Y%m%d%H%M%S') + str(self.id)
        # 自动计算平方数跟室内玻璃的价格
        if self.indoor_real_square == 0.0 and self.indoor_glasses and \
                self.indoor_glasses.area and self.indoor_glasses.area.real_square:
            self.indoor_real_square = self.indoor_glasses.area.real_square * self.indoor_num
            if self.indoor_total_price == 0.0:
                self.indoor_total_price = self.indoor_real_square * self.indoor_glasses.price
        if self.outdoor_real_square == 0.0 and self.outdoor_glasses and self.outdoor_glasses.area.real_square:
            self.outdoor_real_square = self.outdoor_glasses.area.real_square * self.outdoor_num
            if self.indoor_total_price == 0.0:
                self.outdoor_total_price = self.outdoor_real_square * self.outdoor_glasses.price
        if self.real_total_square == 0.0:
            self.real_total_square = self.indoor_real_square + self.outdoor_real_square
        # 自动计算玻璃总价格
        if self.total_price == 0.0:
            self.total_price = self.outdoor_total_price + self.indoor_total_price
        if self.real_total_price == 0.0:
            self.real_total_price = self.total_price
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class BaseOrder(models.Model):
    """
    基础订单表
    """
    status_choices = (
        ('已下单', '已下单'),
        ('已生产', '已生产'),
        ('已采购', '已采购'),
        ('已发货', '已发货'),
        ('客户已收货', '客户已收货'),
        ('订单已完成', '订单已完成'),
    )
    tr_code = models.CharField(max_length=56, unique=True, verbose_name='百叶订单号', null=True, blank=True)
    curtain = models.ForeignKey(Curtain, on_delete=models.CASCADE, verbose_name='百叶序号')
    count = models.IntegerField(verbose_name='数量', default=1)
    total_square = models.FloatField(verbose_name='总平方数(㎡)', default=0.0)
    square_remarks = models.CharField(max_length=256, default='无', verbose_name='平方数差异备注')
    amount = models.FloatField(default=0.0, verbose_name='金额')
    direction = models.ForeignKey(CtrDirection, on_delete=models.CASCADE,
                                  null=True, blank=True, verbose_name='操控器位置')
    install_address = models.CharField(max_length=256, verbose_name='安装位置', null=True, blank=True)
    money_remark = models.CharField(max_length=256, verbose_name='金额信息备注', null=True, blank=True)
    glasses_remark = models.CharField(max_length=256, verbose_name='玻璃信息备注', default='5白钢+19A+5白钢')
    glasses_order = models.ForeignKey(
        GlassOrder, on_delete=models.CASCADE, verbose_name='玻璃订单号', null=True, blank=True)
    glasses_spread = models.FloatField(default=0.0, verbose_name='玻璃差价')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='顾客姓名')
    pay_time = models.DateTimeField(default=datetime.now, verbose_name='客户下单时间')
    plan_time = models.DateTimeField(default=datetime.now, verbose_name='车间计划生产时间')
    reach_time = models.DateTimeField(default=datetime.now, verbose_name='实际发货时间')
    real_amount = models.FloatField(default=0.0, verbose_name='实际金额')
    base_order_status = models.CharField(
        max_length=56, verbose_name='百叶订单状态', choices=status_choices, default='已下单')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='订单创建时间')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='订单更新时间')

    class Meta:
        verbose_name = '百叶订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tr_code

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.tr_code in ('', None):
            self.tr_code = self.create_at.strftime('%Y%m%d%H%M%S') + str(self.id)
        if self.total_square == 0.0:
            # 自动计算总平方数
            self.total_square = round(self.curtain.area.real_square * self.count, 2)
        if self.amount == 0.0:
            # 自动计算价格
            self.amount = round(self.curtain.price * self.total_square, 2)
        if self.real_amount == 0.0:
            self.real_amount = self.amount - self.glasses_spread
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)
