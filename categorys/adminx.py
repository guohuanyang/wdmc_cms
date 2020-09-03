# -*- coding: utf-8 -*-

from categorys.models import Color, CtrDirection, CurtainCat, GlassesCat
from utils.tools import get_all_fields
from categorys.cat_resources import ColorResource, CtrDirectionResource, CurtainCatResource, GlassesCatResource
import xadmin


class ColorAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': ColorResource,
                          'export_resource_class': ColorResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(Color)
    list_filter = ['color']
    search_fields = ['color']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class CtrDirectionAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': CtrDirectionResource,
                          'export_resource_class': CtrDirectionResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(CtrDirection)
    list_filter = ['direction']
    search_fields = ['direction']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class CurtainCatAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': CurtainCatResource,
                          'export_resource_class': CurtainCatResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(CurtainCat)
    list_filter = ['name']
    search_fields = ['name']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class GlassesCatAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': GlassesCatResource,
                          'export_resource_class': GlassesCatResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(GlassesCat)
    list_filter = ['name']
    search_fields = ['name']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


xadmin.site.register(Color, ColorAdmin)
xadmin.site.register(CtrDirection, CtrDirectionAdmin)
xadmin.site.register(CurtainCat, CurtainCatAdmin)
xadmin.site.register(GlassesCat, GlassesCatAdmin)
