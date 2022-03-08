from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    isPaid = models.BooleanField(default=False, verbose_name='پرداخت شده')
    paymentDate = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return self.owner.get_full_name()

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    gheymat = models.IntegerField(verbose_name='قیمت')
    tedad = models.IntegerField(verbose_name='تعداد')

    def get_detail_sum(self):
        return self.gheymat * self.tedad

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'جزئیات سفارش'
        verbose_name_plural = 'جزئیات سفارش'
