import datetime
from django.utils import timezone
from background_task import background
from .models import Store

# just checking

# delete after 10 seconds of function call
@background(schedule=10)
def time_to_live():
    data_list = Store.objects.all()
    for data in data_list:
        try:
            print(data.timestamp+datetime.timedelta(minutes=5))
            # if datetime.now() > data.timestamp + datetime.timedelta(minutes=5):
            #data.value = ''
        except:
            print("error")
