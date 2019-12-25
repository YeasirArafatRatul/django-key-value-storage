import datetime
from rest_framework import generics
from django.utils import timezone
from rest_framework.response import Response

from main_app.models import Store
from .serializers import StoreSerializer
from main_app.tasks import time_to_live


class StoreRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'key'
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def put(self, request, key):
        key = self.kwargs.get("key")
        instance = Store.objects.get(key=key)
        TTL = datetime.timedelta(minutes=5)
        new_time = timezone.now()+TTL
        instance.timestamp = new_time
        instance.save()
        time_to_live(key)
        return super().put(request)

    def patch(self, request, key):
        key = self.kwargs.get("key")
        instance = Store.objects.get(key=key)
        TTL = datetime.timedelta(minutes=5)
        new_time = timezone.now()+TTL
        instance.timestamp = new_time
        instance.save()
        time_to_live(key)
        return super().patch(request)


class allPairsAPI(generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class addAPIView(generics.CreateAPIView):
    lookup_url_kwarg = 'key'
    serializer_class = StoreSerializer

    def create(self, request, key):
        key = self.kwargs.get("key")
        instance = Store.objects.get(key=key)
        TTL = datetime.timedelta(minutes=5)
        new_time = timezone.now()+TTL
        instance.timestamp = new_time
        instance.save()
        time_to_live(key)
        return super().create(request, key)
