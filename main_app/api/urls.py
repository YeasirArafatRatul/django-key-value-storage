from django.urls import path
from .views import StoreRudApiView, allPairsAPI

app_name = "main_app"
urlpatterns = [
    path('single-pair/<str:key>/', StoreRudApiView.as_view(), name='single-pair'),
    path('all-pairs/', allPairsAPI.as_view(), name='all-pairs')

]
