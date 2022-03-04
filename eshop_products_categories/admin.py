from django.contrib import admin
from .models import ProductsCategories
# Register your models here.


@admin.register(ProductsCategories)
class ProductCategoriesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'slug']

    class Meta:
        verbose_name = 'دسته بندی ها'