from django.db import models

# Create your models here.


class Lot(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=200, help_text='Name')
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=(('OPEN', 'open'), ('CANCELED', 'canceled'), ('CLOSED', 'closed')))
    pub_date = models.DateTimeField('date published')




