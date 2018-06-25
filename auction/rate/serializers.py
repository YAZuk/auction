from rest_framework import serializers
from .models import Lot, Rate
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ('first_name', 'last_nam', 'email')
        fields = ('username', )


class LotSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lot
        # fields = ('name', 'description', 'status', 'date_start', 'date_end')
        fields = ('name', )


class RateSerializer(serializers.HyperlinkedModelSerializer):
    lot = LotSerializer(read_only=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Rate
        fields = ('lot', 'price', 'user')

    def create(self, validated_data):
        # return HttpResponse(validated_data, status=201)
        return Rate.objects.create(**validated_data)
        # return validated_data



