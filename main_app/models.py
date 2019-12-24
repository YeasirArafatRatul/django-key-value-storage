from django.db import models

# Create your models here.


class Store(models.Model):
    key = models.CharField(
        max_length=100, primary_key=True, null=False, blank=False, unique=True)
    value = models.CharField(max_length=250, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.key)

    class Meta:
        verbose_name_plural = "Store"
