# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import BaseOrder, GlassOrder, ProductOrder, ShipOrder


@receiver(post_save, sender=BaseOrder)
def create_glass_order(sender, instance=None, created=False, **kwargs):
    if created:
        glass_order_obj = GlassOrder(
            base_order=instance
        )
        glass_order_obj.save()
        product_order_obj = ProductOrder(
            base_order=instance
        )
        product_order_obj.save()
        ship_order_obj = ShipOrder(
            base_order=instance
        )
        ship_order_obj.save()
