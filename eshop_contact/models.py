from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='عنوان')
    email = models.EmailField(max_length=100 , verbose_name='ایمیل')
    subject = models.CharField(max_length=150 , verbose_name='موضوع')
    message = models.TextField( verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ ایجاد')
    isRead = models.BooleanField(default=False , verbose_name='خوانده شده')

    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at}"

    class Meta:
        verbose_name_plural = "تماس ها"
        verbose_name = "تماس"
