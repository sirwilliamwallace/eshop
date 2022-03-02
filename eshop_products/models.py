from django.db import models
import os


# Handle the filename and extension
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


# End of get_filename_ext
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


# Create your models here.
# Product model
# title, description, price, image
class ProductManager(models.Manager):
    """
    Custom manager for the Product model class to add custom methods
    """
    def get_active_products(self):
        return self.get_queryset().filter(active=True)


class Product(models.Model):
    """
    Product model class to represent a product in the database and to store its data in the database table 'products'
    """
    title = models.CharField(max_length=255, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال')
    objects = ProductManager()

    # Meta class for Product model to set the name of the model in the admin panel
    class Meta:
        """
        Meta class for Product model to set the name of the model in the admin panel
        """
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title
