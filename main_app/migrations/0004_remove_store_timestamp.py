# Generated by Django 2.2.4 on 2019-12-26 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20191224_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='timestamp',
        ),
    ]
