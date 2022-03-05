from django.contrib import admin
from .models import Slider


# Register your models here.
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'link')
