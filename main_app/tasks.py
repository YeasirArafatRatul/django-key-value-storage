import datetime
from django.utils import timezone
from background_task import background
from .models import Store

# just checking


@background(schedule=320)
def time_to_live(key):
    obj = Store.objects.get(key=key)
    data = obj.timestamp
    print(data)
    current_time = timezone.now()
    try:
        if current_time > obj.timestamp:
            obj.value = ''
            obj.save()
    except:
        print("error")


# def time_to_live():
#     data_list = Store.objects.all()

#     for data in data_list:
#         current_time = timezone.now()
#         try:
#             if current_time > data.timestamp + datetime.timedelta(minutes=5):
#                 data.value = ''
#                 data.save()
#                 # key = self.kwargs.get("key")
#                 # instance = Store.objects.get(key=key)
#                 # TTL = datetime.timedelta(minutes=5)
#                 # new_time = timezone.now()+TTL
#                 # instance.timestamp = new_time
#                 # instance.save()
#                 # print(data.timestamp)
#                 # print("\n")
#         except:
#             print("error")
