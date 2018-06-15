from rest_framework import serializers
from .models import Lot


class LotSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lot
        fields = ('name', 'description', 'status', 'date_start', 'date_end')

