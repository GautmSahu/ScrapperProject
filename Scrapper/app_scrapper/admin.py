from django.contrib import admin
from app_scrapper.models import *


class ProxyModelAdmin(admin.ModelAdmin):
    list_display = ('country', 'ip', 'port', 'protocol', 'uptime', 'created_datetime')


admin.site.register(ProxyModel, ProxyModelAdmin)