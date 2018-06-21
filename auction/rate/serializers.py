from rest_framework import serializers
from .models import Lot, Rate


class LotSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lot
        fields = ('id', 'name', 'description', 'status', 'date_start', 'date_end')


class RateSerializer(serializers.HyperlinkedModelSerializer):
    lot = LotSerializer()

    class Meta:
        model = Rate
        fields = ('id', 'lot', 'price', 'pub_date')




