from django.contrib import admin
from .models import Lot, Rate, WinnerLot

# Register your models here.
admin.site.register(Lot)
admin.site.register(Rate)
admin.site.register(WinnerLot)
