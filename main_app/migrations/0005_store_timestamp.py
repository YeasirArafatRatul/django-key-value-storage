# Generated by Django 2.2.4 on 2019-12-26 09:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_store_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 9, 26, 34, 293924, tzinfo=utc)),
        ),
    ]
