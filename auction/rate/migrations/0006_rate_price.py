# Generated by Django 2.1a1 on 2018-06-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0005_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
