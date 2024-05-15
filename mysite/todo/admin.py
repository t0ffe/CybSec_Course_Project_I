from django.contrib import admin

# Register your models here.

from .models import *
from .flags import safe

admin.site.register(Todo)

if safe:
    @admin.register(AuditEntry)
    class AuditEntryAdmin(admin.ModelAdmin):
        list_display = ['action', 'username',]
        list_filter = ['action',]
else:
    admin.site.register(UnsafeUser)