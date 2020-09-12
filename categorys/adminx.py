# -*- coding: utf-8 -*-

import xadmin
from xadmin import views
from categorys.models import Color, CurtainCat
from utils.tools import get_all_fields
from categorys.cat_resources import ColorResource, CurtainCatResource
from others.models import Customer, GlassesFactory
from xadmin.models import Log
from orders.models import BaseOrder, GlassOrder, ProductOrder, ShipOrder
from django.contrib.auth.models import Group, Permission, User


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
                    {'title': '客户订单', 'url': self.get_model_url(BaseOrder, 'changelist')},
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
                    {'title': '采购订单', 'url': self.get_model_url(GlassOrder, 'changelist')},
                    {'title': '钢化厂管理', 'url': self.get_model_url(GlassesFactory, 'changelist')},
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
                     'url': self.get_model_url(ProductOrder, 'changelist')},
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
                    {'title': '仓库发货订单', 'url': self.get_model_url(ShipOrder, 'changelist')},
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


xadmin.site.register(Color, ColorAdmin)
xadmin.site.register(CurtainCat, CurtainCatAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
