from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
from eshop_products.models import Product
from .utils import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='اسلاگ')
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title


def tag_presave_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_presave_receiver, sender=Tag)
