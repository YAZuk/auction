# Generated by Django 2.1a1 on 2018-06-15 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0006_rate_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='lot',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 10, 32, 7, 364387)),
        ),
        migrations.AddField(
            model_name='lot',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 10, 32, 7, 364354)),
        ),
    ]