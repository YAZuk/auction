# Generated by Django 2.1a1 on 2018-06-15 10:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0011_auto_20180615_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 10, 56, 26, 435253)),
        ),
        migrations.AlterField(
            model_name='lot',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 10, 56, 26, 435207)),
        ),
        migrations.AlterField(
            model_name='winnerlot',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 6, 15, 10, 56, 26, 436550, tzinfo=utc)),
        ),
    ]
