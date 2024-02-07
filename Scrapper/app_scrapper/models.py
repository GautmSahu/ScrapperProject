from django.db import models
from django.utils import timezone


class ProxyModel(models.Model):
    ip = models.CharField(max_length=15, help_text="Ip address.", blank=True, null=True)
    port = models.IntegerField(help_text="Port no.", blank=True, null=True)
    protocol = models.CharField(max_length=20, help_text="Protocol.", blank=True, null=True)
    country = models.CharField(max_length=50, help_text="Country name.", blank=True, null=True)
    uptime = models.CharField(max_length=50, help_text="Uptime.", blank=True, null=True)
    created_datetime = models.DateTimeField(default=timezone.now, help_text="Created datetime.", blank=True, null=True)

    class Meta:
        verbose_name = 'ProxyModel'
        verbose_name_plural = 'ProxyModels'
