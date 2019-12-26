from rest_framework import serializers
from main_app.models import Store

# converting to json and validation for passed data+


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['key', 'value', ]
