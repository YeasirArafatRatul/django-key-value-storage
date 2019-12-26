# Generated by Django 2.2.4 on 2019-12-26 16:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_store_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 17, 4, 58, 734941, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='store',
            name='value',
            field=models.TextField(),
        ),
    ]