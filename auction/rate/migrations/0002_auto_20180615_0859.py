# Generated by Django 2.1a1 on 2018-06-15 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lot',
            options={'ordering': ['name']},
        ),
    ]
