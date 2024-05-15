from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Todo)
admin.site.register(UnsafeUser)
'''
@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ['action', 'username',]
    list_filter = ['action',]
'''