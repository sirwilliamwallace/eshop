from django.db import models

# Create your models here.
class ProductsCategories(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
