from django.contrib import admin
from main_app.models import Store
# Register your models here.


class ModelStore(admin.ModelAdmin):
    list_display = ['key', 'value', 'timestamp']


admin.site.register(Store, ModelStore)
