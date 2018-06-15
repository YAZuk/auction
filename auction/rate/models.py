from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Lot(models.Model):

    class Meta:
        ordering = ['name']
        verbose_name = "Лот"
        verbose_name_plural = "Лоты"

    name = models.CharField(max_length=200, help_text='Name')
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=(('OPEN', 'open'), ('CANCELED', 'canceled'), ('CLOSED', 'closed')))
    pub_date = models.DateTimeField('date published')


class Rate(models.Model):

    class Meta:
        ordering = ['pub_date']
        verbose_name = "Ставка"
        verbose_name_plural = "Ставки"

    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)




