
from django.contrib import admin
from django.urls import path, include
from background_task.models import Task
from main_app.tasks import time_to_live
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main_app.api.urls')),
]
# time_to_live(repeat=360)  # five_minutes
