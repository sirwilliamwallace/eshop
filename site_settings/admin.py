from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.SiteSetting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ["__str__", "site_title",]

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "کلیه تنظیمات سایت"
