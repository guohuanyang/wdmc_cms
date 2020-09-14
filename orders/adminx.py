# -*- coding: utf-8 -*-

from orders.models import BaseOrder, GlassOrder, ProductOrder, ShipOrder
from utils.tools import get_all_fields
from orders.orders_resouce import BaseOrderResource, GlassOrderResource, ProductOrderResource, ShipOrderResource
import xadmin


class BaseOrderAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': BaseOrderResource,
                          'export_resource_class': BaseOrderResource}
    # import_export_args = {'import_resource_class': BaseOrderResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = ['tr_code', 'tax_float', 'total_money', 'has_received', 'pay_time', 'width', 'height', 'count',
                    'single_square', 'total_square', 'single_price', 'detail_remark', 'color', 'category',
                    'customer', 'address', 'real_single_square', 'real_total_square', 'indoor_glasses',
                    'outdoor_glasses', 'status', 'glass_status', 'produced_time', 'ship_num', 'ship_time',
                    'un_ship_num']
    list_filter = ['tr_code', 'status', 'total_money', 'pay_time', 'width', 'height', 'total_square',
                   'detail_remark', 'color__color', 'category__name', 'customer__name', 'address',
                   'indoor_glasses', 'outdoor_glasses']
    search_fields = ['tr_code', 'status', 'total_money', 'pay_time', 'width', 'height', 'total_square',
                     'detail_remark', 'color__color', 'category__name', 'customer__name', 'address', 'indoor_glasses',
                     'outdoor_glasses']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['tr_code']

    def glass_status(self, obj):
        glass_order = GlassOrder.objects.filter(base_order=obj).first()
        if glass_order:
            return str(glass_order.status)
        else:
            return '无采购订单'
    glass_status.short_description = '采购状态'

    def produced_time(self, obj):
        product_order = ProductOrder.objects.filter(base_order=obj).first()
        if product_order:
            if product_order.product_time:
                return product_order.product_time
            else:
                return ''
        else:
            return '无生产订单'
    produced_time.short_description = '生产时间'

    def ship_num(self, obj):
        ship_order = ShipOrder.objects.filter(base_order=obj).first()
        if ship_order:
            return str(ship_order.ship_num)
        else:
            return '无仓库订单'
    ship_num.short_description = '发货数量'

    def ship_time(self, obj):
        ship_order = ShipOrder.objects.filter(base_order=obj).first()
        if ship_order.ship_time:
            return str(ship_order.ship_time)
        else:
            return ''
    ship_time.short_description = '发货时间'

    def un_ship_num(self, obj):
        ship_order = ShipOrder.objects.filter(base_order=obj).first()
        if ship_order:
            return str(ship_order.un_ship_num)
        else:
            return '0'
    un_ship_num.short_description = '未发货数量'


class GlassOrderAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': GlassOrderResource,
                          'export_resource_class': GlassOrderResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(GlassOrder)
    list_filter = []
    search_fields = []
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_editable = ['status']
    list_display_links = ['id']


class ProductOrderAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': ProductOrderResource,
                          'export_resource_class': ProductOrderResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(ProductOrder)
    list_filter = []
    search_fields = []
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_editable = ['has_produced', 'produced_num', 'un_produced_num']
    list_display_links = ['id']


class ShipOrderAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': ShipOrderResource,
                          'export_resource_class': ShipOrderResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(ShipOrder)
    list_filter = []
    search_fields = []
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_editable = ['has_shipped', 'ship_num', 'un_ship_num']
    list_display_links = ['id']


xadmin.site.register(BaseOrder, BaseOrderAdmin)
xadmin.site.register(GlassOrder, GlassOrderAdmin)
xadmin.site.register(ProductOrder, ProductOrderAdmin)
xadmin.site.register(ShipOrder, ShipOrderAdmin)
