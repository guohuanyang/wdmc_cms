# -*- coding: utf-8 -*-

from import_export import resources
from utils.tools import get_all_fields

from goods.models import Curtain, IndoorGlasses, OutdoorGlasses


class CurtainResource(resources.ModelResource):
    def __init__(self):
        super(CurtainResource, self).__init__()

        field_list = Curtain._meta.fields
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
        model = Curtain
        exclude = ('id',)
        # import_id_fields = ('num', )
        # print(get_all_fields(ALastMonthTest))
        import_id_fields = get_all_fields(Curtain)


class IndoorGlassesResource(resources.ModelResource):
    def __init__(self):
        super(IndoorGlassesResource, self).__init__()

        field_list = IndoorGlasses._meta.fields
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
        model = IndoorGlasses
        exclude = ('id',)
        # import_id_fields = ('num', )
        # print(get_all_fields(ALastMonthTest))
        import_id_fields = get_all_fields(IndoorGlasses)


class OutdoorGlassesResource(resources.ModelResource):
    def __init__(self):
        super(OutdoorGlassesResource, self).__init__()

        field_list = OutdoorGlasses._meta.fields
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
        model = OutdoorGlasses
        exclude = ('id',)
        # import_id_fields = ('num', )
        # print(get_all_fields(ALastMonthTest))
        import_id_fields = get_all_fields(OutdoorGlasses)
