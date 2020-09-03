# -*- coding: utf-8 -*-

from orders.models import BaseOrder, GlassOrder
from utils.tools import get_all_fields
from orders.orders_resouce import BaseOrderResource, GlassOrderResource
import xadmin


class BaseOrderAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': BaseOrderResource,
                          'export_resource_class': BaseOrderResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(BaseOrder)
    list_filter = ['real_amount', 'tr_code', 'base_order_status']
    search_fields = ['real_amount', 'tr_code']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class GlassOrderAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': GlassOrderResource,
                          'export_resource_class': GlassOrderResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(GlassOrder)
    list_filter = ['tr_code']
    search_fields = ['tr_code']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class ProductionAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': GlassOrderResource,
                          'export_resource_class': GlassOrderResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(GlassOrder)
    list_filter = ['tr_code']
    search_fields = ['tr_code']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


xadmin.site.register(BaseOrder, BaseOrderAdmin)
xadmin.site.register(GlassOrder, GlassOrderAdmin)
