# -*- coding: utf-8 -*-
import collections
from import_export import resources
from utils.tools import get_all_fields
from import_export.fields import Field
from orders.models import BaseOrder, GlassOrder, ProductOrder, ShipOrder
from categorys.models import Color, CurtainCat
from others.models import Customer


class BaseOrderResource(resources.ModelResource):
    glass_status = Field(attribute='采购状态', column_name='glass_status')
    produced_time = Field(attribute='生产时间', column_name='produced_time')
    ship_num = Field(attribute='发货数量', column_name='ship_num')
    ship_time = Field(attribute='发货时间', column_name='ship_time')
    un_ship_num = Field(attribute='未发货数量', column_name='un_ship_num')
    # color = Field(attribute='color__color', column_name='颜色')
    # category = Field(attribute='category__name', column_name='类别')
    # customer = Field(attribute='customer__name', column_name='客户')

    def __init__(self):
        super(BaseOrderResource, self).__init__()
        field_list = BaseOrder._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    # # 默认导入导出field的column_name为字段的名称，这里修改为字段的verbose_name
    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
            else:
                field.column_name = field.attribute
        return fields

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        pass

    def after_import_instance(self, instance, new, **kwargs):
        pass

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        temp_dict = []
        for row in dataset.dict:
            tmp = collections.OrderedDict()
            for key in row:
                if key == '颜色':
                    color, status = Color.objects.get_or_create(color=row[key])
                    tmp['颜色'] = color.id
                elif key == '产品类型':
                    category, status = CurtainCat.objects.get_or_create(name=row[key])
                    tmp['产品类型'] = category.id
                elif key == '客户':
                    customer, status = Customer.objects.get_or_create(name=row[key])
                    tmp['客户'] = customer.id
                else:
                    tmp[key] = row[key]
            temp_dict.append(tmp)
        dataset.dict = temp_dict
        return dataset

    def after_export(self, queryset, data, *args, **kwargs):
        temp_dict = []
        for row in data.dict:
            tmp = collections.OrderedDict()
            print(row)
            for key in row:
                print(key, row[key])
                if key == '颜色':
                    color= Color.objects.get(id=row[key])
                    tmp['颜色'] = color.color
                elif key == '产品类型':
                    category= CurtainCat.objects.get(id=row[key])
                    tmp['产品类型'] = category.name
                elif key == '客户':
                    customer= Customer.objects.get(id=row[key])
                    tmp['客户'] = customer.name
                else:
                    tmp[key] = row[key]
            temp_dict.append(tmp)
        data.dict = temp_dict
        return data

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None

    class Meta:
        model = BaseOrder
        skip_unchanged = True
        report_skipped = True
        exclude = ('id', 'last_update_time')
        # import_id_fields = ('tr_code',)
        fields = ('tr_code', 'tax_float', 'total_money', 'has_received', 'pay_time', 'width', 'height',
                  'count', 'min_square', 'single_square', 'total_square', 'single_price', 'detail_remark', 'color',
                  'category', 'customer', 'address', 'real_single_square', 'real_total_square',
                  'indoor_glasses',  'outdoor_glasses', 'status', 'glass_status', 'produced_time',
                  'ship_num', 'ship_time', 'un_ship_num')
        export_order = ('tr_code', 'tax_float', 'total_money', 'has_received', 'pay_time', 'width', 'height',
                        'count', 'min_square', 'single_square', 'total_square', 'single_price', 'detail_remark', 'color',
                        'category', 'customer', 'address', 'real_single_square', 'real_total_square',
                        'indoor_glasses',  'outdoor_glasses', 'status', 'glass_status', 'produced_time',
                        'ship_num', 'ship_time', 'un_ship_num')

    def dehydrate_glass_status(self, base_order):
        glass_order = GlassOrder.objects.filter(base_order=base_order).first()
        if glass_order:
            return str(glass_order.status)
        else:
            return '无采购订单'
    dehydrate_glass_status.short_description = '采购状态'

    def dehydrate_produced_time(self, base_order):
        product_order = ProductOrder.objects.filter(base_order=base_order).first()
        if product_order:
            if product_order.product_time:
                return product_order.product_time
            else:
                return ''
        else:
            return '无生产订单'
    dehydrate_produced_time.short_description = '生产时间'

    def dehydrate_ship_num(self, base_order):
        ship_order = ShipOrder.objects.filter(base_order=base_order).first()
        if ship_order:
            return str(ship_order.ship_num)
        else:
            return '无仓库订单'
    dehydrate_ship_num.short_description = '发货数量'

    def dehydrate_ship_time(self, base_order):
        ship_order = ShipOrder.objects.filter(base_order=base_order).first()
        if ship_order:
            return str(ship_order.ship_time)
        else:
            return '无仓库订单'
    dehydrate_ship_time.short_description = '发货时间'

    def dehydrate_un_ship_num(self, base_order):
        ship_order = ShipOrder.objects.filter(base_order=base_order).first()
        if ship_order:
            return str(ship_order.un_ship_num)
        else:
            return '无仓库订单'
    dehydrate_un_ship_num.short_description = '未发货数量'


class GlassOrderResource(resources.ModelResource):
    def __init__(self):
        super(GlassOrderResource, self).__init__()

        field_list = GlassOrder._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    # 默认导入导出field的column_name为字段的名称，这里修改为字段的verbose_name
    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        pass

    def after_import_instance(self, instance, new, **kwargs):
        pass

    class Meta:
        model = GlassOrder
        exclude = ('id',)
        # import_id_fields = ('num', )
        # print(get_all_fields(ALastMonthTest))
        import_id_fields = get_all_fields(GlassOrder)


class ProductOrderResource(resources.ModelResource):
    def __init__(self):
        super(ProductOrderResource, self).__init__()

        field_list = ProductOrder._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    # 默认导入导出field的column_name为字段的名称，这里修改为字段的verbose_name
    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        pass

    def after_import_instance(self, instance, new, **kwargs):
        pass

    class Meta:
        model = ProductOrder
        exclude = ('id',)
        # import_id_fields = ('num', )
        # print(get_all_fields(ALastMonthTest))
        import_id_fields = get_all_fields(ProductOrder)


class ShipOrderResource(resources.ModelResource):
    def __init__(self):
        super(ShipOrderResource, self).__init__()

        field_list = ShipOrder._meta.fields
        self.vname_dict = {}
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name

    # 默认导入导出field的column_name为字段的名称，这里修改为字段的verbose_name
    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # 如果我们设置过verbose_name，则将column_name替换为verbose_name。否则维持原有的字段名
            if field_name in self.vname_dict.keys():
                field.column_name = self.vname_dict[field_name]
        return fields

    def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
        pass

    def after_import_instance(self, instance, new, **kwargs):
        pass

    class Meta:
        model = ShipOrder
        exclude = ('id',)
        # import_id_fields = ('num', )
        # print(get_all_fields(ALastMonthTest))
        import_id_fields = get_all_fields(ShipOrder)
