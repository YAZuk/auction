from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

# Create your models here.


class Lot(models.Model):

    class Meta:
        ordering = ['name']
        verbose_name = "Лот"
        verbose_name_plural = "Лоты"

    name = models.CharField(max_length=200, help_text='Name')
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=(('OPEN', 'open'), ('CANCELED', 'canceled'), ('CLOSED', 'closed')))
    date_start = models.DateTimeField(default=django.utils.timezone.now)
    date_end = models.DateTimeField(default=django.utils.timezone.now)
    pub_date = models.DateTimeField(default=django.utils.timezone.now)


class Rate(models.Model):

    class Meta:
        ordering = ['pub_date']
        verbose_name = "Ставка"
        verbose_name_plural = "Ставки"

    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=django.utils.timezone.now)
    price = models.IntegerField(default=100)

    # def __str__(self):
    #     return lot.name


class WinnerLot(models.Model):

    class Meta:
        ordering = ['user']
        verbose_name = "Победитель лота"
        verbose_name_plural = "Победители аукциона"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.ForeignKey(Rate, on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)


