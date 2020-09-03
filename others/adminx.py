# -*- coding: utf-8 -*-

import xadmin
from others.models import Customer, GlassesFactory
from others.other_resource import CustomerResource, GlassesFactoryResource
from utils.tools import get_all_fields


class CustomerAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': CustomerResource,
                          'export_resource_class': CustomerResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(Customer)
    list_filter = ['name']
    search_fields = ['name']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class GlassesFactoryAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': GlassesFactoryResource,
                          'export_resource_class': GlassesFactoryResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(GlassesFactory)
    list_filter = ['name']
    search_fields = ['name']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


xadmin.site.register(Customer, CustomerAdmin)
xadmin.site.register(GlassesFactory, GlassesFactoryAdmin)
