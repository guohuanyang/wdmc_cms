# Create your models here.
from others.models import Customer, GlassesFactory
from categorys.models import CurtainCat, Color
from django.db import models
from datetime import datetime


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
    tr_code = models.CharField(max_length=56, unique=True, verbose_name='百叶订单号(pc)', null=True, blank=True)
    tax_float = models.FloatField(default=0.06, verbose_name='税点')
    total_money = models.FloatField(default=0.0, verbose_name='总金额')
    has_received = models.FloatField(default=0.0, verbose_name='已收款')
    auto_calculate = models.BooleanField(default=True, verbose_name='电脑自动计算金额')
    pay_time = models.DateTimeField(default=datetime.now, verbose_name='下单时间')
    width = models.FloatField(default=0.0, verbose_name='宽(W)mm')
    height = models.FloatField(default=0.0, verbose_name='高(H)mm')
    count = models.IntegerField(default=1, verbose_name='数量')
    single_square = models.FloatField(default=0.0, verbose_name='单件平方数(㎡)')
    real_single_square = models.FloatField(default=0.0, verbose_name='实际单件平方数(㎡)(pc)')
    total_square = models.FloatField(default=0.0, verbose_name='总平方数(㎡)(pc)')
    real_total_square = models.FloatField(default=0.0, verbose_name='实际总平方数(㎡)(pc)')
    single_price = models.FloatField(default=0.0, verbose_name='单价')
    detail_remark = models.CharField(max_length=256, default='', verbose_name='明细备注')
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE, verbose_name='颜色')
    category = models.ForeignKey(to=CurtainCat, on_delete=models.CASCADE, verbose_name='产品类型')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='客户')
    address = models.CharField(max_length=256, default='', verbose_name='送货位置')
    indoor_glasses = models.CharField(max_length=256, default='5白钢', verbose_name='室内玻璃')
    outdoor_glasses = models.CharField(max_length=256, default='5白钢', verbose_name='室外玻璃')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='订单创建日期')
    status = models.CharField(
        max_length=56, verbose_name='订单状态', choices=status_choices, default='已下单')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='订单更新时间')

    class Meta:
        verbose_name = '百叶订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.tr_code)

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        if self.tr_code in ('', None):
            self.tr_code = self.create_at.strftime('%Y%m%d%H%M%S') + str(self.id)
        if self.auto_calculate:
            # 实际平方
            self.real_single_square = self.single_square
            # 自动计算总平方数
            self.total_square = round(self.single_square * self.count, 2)
            # 实际总平方数
            self.real_total_square = self.total_square
            # 自动计算价格
            self.total_money = round(self.single_price * self.real_total_square, 2)
            self.last_update_time = datetime.now()

        super().save(*args, **kwargs)


class GlassOrder(models.Model):
    """
    玻璃订单表
    """
    status_choices = (
        ("未采购", "未采购"),
        ("已下单", "已下单"),
        ("已完成", "已完成"),
    )
    base_order = models.ForeignKey(BaseOrder, on_delete=models.CASCADE, verbose_name='客户订单')

    indoor_single_price = models.FloatField(default=0.0, verbose_name='单价')
    indoor_total_money = models.FloatField(default=0.0, verbose_name='金额')
    indoor_factory = models.ForeignKey(
        GlassesFactory, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='钢化厂(室内玻璃)', related_name='f_indoor_factory')
    indoor_pay_time = models.DateTimeField(default=None, blank=True, null=True, verbose_name='下单时间(室内玻璃)')

    outdoor_single_price = models.FloatField(default=0.0, verbose_name='单价')
    outdoor_total_money = models.FloatField(default=0.0, verbose_name='金额')
    outdoor_factory = models.ForeignKey(
        GlassesFactory, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='钢化厂(室外玻璃)', related_name='f_outdoor_factory')
    outdoor_pay_time = models.DateTimeField(default=None, blank=True, null=True, verbose_name='下单时间(室外玻璃)')

    total_money = models.FloatField(default=0.0, verbose_name='总金额')
    status = models.CharField(
        max_length=56, verbose_name='玻璃订单状态', choices=status_choices, default='未下单')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='玻璃订单创建日期')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '玻璃订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        if self.base_order.auto_calculate:
            self.indoor_total_money = round(self.indoor_single_price * self.base_order.real_total_square, 2)
            self.outdoor_total_money = round(self.outdoor_single_price * self.base_order.real_total_square, 2)
            self.total_money = self.indoor_total_money + self.outdoor_total_money
        super().save(*args, **kwargs)


class ProductOrder(models.Model):
    """
    生产进度表
    """
    base_order = models.ForeignKey(BaseOrder, on_delete=models.CASCADE, verbose_name='客户订单')
    product_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name='车间生产时间')
    produced_num = models.IntegerField(default=0, verbose_name='车间完成数量')
    un_produced_num = models.IntegerField(default=0, verbose_name='车间未完成数量')
    has_produced = models.BooleanField(default=False, verbose_name='是否完成生产')
    product_remark = models.CharField(max_length=256, default='无', verbose_name='未生产备注')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='生产进度单创建日期')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='生产进度单更新时间')

    class Meta:
        verbose_name = '生产进度单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        if self.has_produced:
            self.base_order.status = '已生产'
            self.base_order.save()
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)


class ShipOrder(models.Model):
    """
    仓库发货表
    """
    base_order = models.ForeignKey(BaseOrder, on_delete=models.CASCADE, verbose_name='客户订单')
    ship_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name='发货日期')
    ship_num = models.IntegerField(default=0, verbose_name='发货数量')
    un_ship_num = models.IntegerField(default=0, verbose_name='未发货数量')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='发货进度单创建日期')
    has_shipped = models.BooleanField(default=False, verbose_name='是否完成发货')
    ship_remark = models.CharField(max_length=256, default='无', verbose_name='未发货备注')
    last_update_time = models.DateTimeField(default=datetime.now, verbose_name='发货进度单更新时间')

    class Meta:
        verbose_name = '仓库发货单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        if self.has_shipped and self.base_order.status == '已生产':
            self.base_order.status = '已发货'
            self.base_order.save()
        self.last_update_time = datetime.now()
        super().save(*args, **kwargs)
