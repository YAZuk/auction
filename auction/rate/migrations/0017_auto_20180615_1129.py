# Generated by Django 2.1a1 on 2018-06-15 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0016_remove_winnerlot_lot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]