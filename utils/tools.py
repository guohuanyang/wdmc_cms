# -*- coding: utf-8 -*-


def get_all_fields(orm_model):
    s = [field.name for field in orm_model._meta.local_fields]
    return s
