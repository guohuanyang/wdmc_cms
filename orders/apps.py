from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'
    verbose_name = '订单管理'
    verbose_name_plural = verbose_name

    def ready(self):
        import orders.order_signal
