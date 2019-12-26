import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Store(models.Model):
    key = models.CharField(
        max_length=100, primary_key=True, null=False, blank=False, unique=True)
    value = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(
        default=timezone.now() + datetime.timedelta(minutes=5))

    def __str__(self):
        return str(self.key)

    class Meta:
        verbose_name_plural = "Store"
