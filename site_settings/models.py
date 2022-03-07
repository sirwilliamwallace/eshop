from django.db import models


# Create your models here.
class SiteSetting(models.Model):
    site_title = models.CharField(max_length=100, verbose_name='عنوان سایت')
    site_address = models.CharField(max_length=100, verbose_name='آدرس سایت')
    site_email = models.EmailField(verbose_name='ایمیل سایت')
    site_phone = models.CharField(max_length=20, verbose_name='شماره تلفن سایت')
    site_fax = models.CharField(max_length=20, verbose_name='شماره فکس سایت')
    site_logo = models.ImageField(upload_to='site_logo', verbose_name='لوگوی سایت')
    site_description = models.TextField(verbose_name='توضیحات سایت')
    copyright_text = models.CharField(max_length=100, verbose_name='متن حق تکثیر')

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "کل تنظیمات سایت"
