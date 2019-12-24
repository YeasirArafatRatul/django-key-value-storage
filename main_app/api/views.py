from rest_framework import generics
from main_app.models import Store
from .serializers import StoreSerializer


class StoreRudApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'key'
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    # def get_queryset(self):
    #     return Store.objects.all()

    # def get_object(self):
    #     key = self.kwargs.get("key")
    #     return Store.objects.get(pk=key)


class allPairsAPI(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
