from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at', 'isRead',)
    list_filter = ('isRead', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('isRead',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
