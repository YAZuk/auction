from rest_framework import serializers
from .models import Lot, Rate
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class LotSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lot
        fields = ('name', 'description', 'status', 'date_start', 'date_end')


class RateSerializer(serializers.HyperlinkedModelSerializer):
    lot = LotSerializer(read_only=False)
    user = UserSerializer(read_only=False)

    class Meta:
        model = Rate
        fields = ('lot', 'user', 'price')

    def create(self, validated_data):
        print(validated_data)
        print(User.objects.all())




