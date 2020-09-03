# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         adminx
# Description:  
# Author:       guohuanyang
# Date:         2020/7/6
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import xadmin
from xadmin import views
from goods.models import Curtain, IndoorGlasses, OutdoorGlasses, Area
from others.models import Customer, GlassesFactory
from xadmin.models import Log
from categorys.models import Color, CtrDirection, CurtainCat, GlassesCat
from orders.models import BaseOrder, GlassOrder
from django.contrib.auth.models import Group, Permission, User
from goods.goods_resources import CurtainResource, IndoorGlassesResource, OutdoorGlassesResource
from utils.tools import get_all_fields


# Register your models here.
class BaseSetting(object):
    enable_themes = True  # 开启主题选择
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "威盾节能玻璃"  # 设置左上角title名字
    site_footer = "guohuanyang"  # 设置底部关于版权信息
    # 设置菜单缩放
    menu_style = "accordion"     # 设置菜单样式

    def get_site_menu(self):
        return [
            {
                'title': '业务下单',
                'icon': 'fa fa-home',
                # 'perm': self.get_model_perm(Poll, 'change'),
                'menus': (
                    {'title': '订单管理', 'url': self.get_model_url(BaseOrder, 'changelist')},
                    {'title': '客户管理', 'url': self.get_model_url(Customer, 'changelist')},
                    # {'title': '玻璃订单', 'url': self.get_model_url(GlassOrder, 'changelist')},
                    # {'title': '生产车间订单',
                    #  'url': self.get_model_url(BaseOrder, 'changelist')+'?_p_base_order_status__exact=已下单'},
                )
            },
            {
                'title': '采购下单',
                'icon': 'fa fa-home',
                # 'perm': self.get_model_perm(Poll, 'change'),
                'menus': (
                    # {'title': '颜色', 'url': self.get_model_url(Color, 'changelist')},
                    # {'title': '控制器位置', 'url': self.get_model_url(CtrDirection, 'changelist')},
                    # {'title': '百叶类别', 'url': self.get_model_url(CurtainCat, 'changelist')},
                    # {'title': '玻璃类别', 'url': self.get_model_url(GlassesCat, 'changelist')},
                )
            },
            {
                'title': '生产进度',
                'icon': 'fa fa-home',
                # 'perm': self.get_model_perm(Poll, 'change'),
                'menus': (
                    {'title': '生产车间订单',
                     'url': self.get_model_url(BaseOrder, 'changelist') + '?_p_base_order_status__exact=已下单'},
                    # {'title': '长宽信息', 'url': self.get_model_url(Area, 'changelist')},
                    # {'title': '百叶', 'url': self.get_model_url(Curtain, 'changelist')},
                    # {'title': '室内玻璃', 'url': self.get_model_url(IndoorGlasses, 'changelist')},
                    # {'title': '室外玻璃', 'url': self.get_model_url(OutdoorGlasses, 'changelist')},
                )
            },
            {
                'title': '仓库发货',
                'icon': 'fa fa-home',
                # 'perm': self.get_model_perm(Poll, 'change'),
                'menus': (
                    # {'title': '客户', 'url': self.get_model_url(Customer, 'changelist')},
                    # {'title': '钢化产', 'url': self.get_model_url(GlassesFactory, 'changelist')},
                )
            },
            {
                'title': '权限管理',
                'icon': 'fa fa-cog',
                # 'perm': self.get_model_perm(Poll, 'change'),
                'menus': (
                    {'title': '用户信息', 'url': self.get_model_url(User, 'changelist')},
                    {'title': '权限信息', 'url': self.get_model_url(Permission, 'changelist')},
                    {'title': '角色信息', 'url': self.get_model_url(Group, 'changelist')},
                    {'title': '日志信息', 'url': self.get_model_url(Log, 'changelist')},
                )
            },
        ]


class CurtainAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': CurtainResource,
                          'export_resource_class': CurtainResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(Curtain)
    list_filter = ['name', 'price']
    search_fields = ['name']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class IndoorGlassesAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': IndoorGlassesResource,
                          'export_resource_class': IndoorGlassesResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(IndoorGlasses)
    list_filter = ['name', 'price']
    search_fields = ['name']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class OutdoorGlassesAdmin(object):
    # 开启import_export导出导出功能
    import_export_args = {'import_resource_class': OutdoorGlassesResource,
                          'export_resource_class': OutdoorGlassesResource}
    list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(OutdoorGlasses)
    list_filter = ['name', 'price']
    search_fields = ['name']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


class AreaAdmin(object):
    # 开启import_export导出导出功能
    # import_export_args = {'import_resource_class': OutdoorGlassesResource,
    #                       'export_resource_class': OutdoorGlassesResource}
    # list_export = {}
    model_icon = 'fa fa-home'
    list_display = get_all_fields(Area)
    list_filter = ['id', 'square']
    search_fields = ['name']
    # ordering = ('-sold_num_chn',)
    list_per_page = 25
    list_display_links = ['id']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Area, AreaAdmin)
xadmin.site.register(Curtain, CurtainAdmin)
xadmin.site.register(IndoorGlasses, IndoorGlassesAdmin)
xadmin.site.register(OutdoorGlasses, OutdoorGlassesAdmin)
