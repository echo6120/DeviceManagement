from audioop import reverse


from django.db import models
from django.utils import timezone


class DeviceSystem(models.Model):
    #Android or iOS or sth
    System = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.System

#设备
class Device(models.Model):
    device_system = models.ForeignKey(DeviceSystem, on_delete=models.CASCADE, related_name="device")
    device_name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    borrow = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-id",)
        index_together = (('id', 'device_name'),)

    def __str__(self):
        return self.title
