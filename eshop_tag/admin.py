from django.contrib import admin

# Register your models here.
from eshop_tag.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')

