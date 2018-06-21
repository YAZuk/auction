from rest_framework import serializers
from .models import Lot, Rate
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')


class LotSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lot
        fields = ('id', 'name', 'description', 'status', 'date_start', 'date_end')


class RateSerializer(serializers.HyperlinkedModelSerializer):
    lot = LotSerializer()
    user = UserSerializer()

    class Meta:
        model = Rate
        fields = ('id', 'lot', 'price', 'pub_date', 'user')




