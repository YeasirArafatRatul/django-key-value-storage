from django.urls import path
from .views import StoreRUDApiView, allPairsAPI, addAPIView

app_name = "main_app"
urlpatterns = [
    path('single-pair/<str:key>/', StoreRUDApiView.as_view(), name='single-pair'),
    path('all-pairs/', allPairsAPI.as_view(), name='all-pairs'),
    path('create/', addAPIView.as_view(), name='create')
]
