from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import LotSerializer, RateSerializer
from .models import Lot, Rate, WinnerLot
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return HttpResponse("Rate")


class LotActiveList(generics.ListCreateAPIView):
    """
    """
    model = Lot
    serializer_class = LotSerializer
    queryset = Lot.objects.filter(status="OPEN")


class CreateRate(generics.ListCreateAPIView):
    """
    """
    model = Rate
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def perform_create(self, serializer):
        post_request = serializer.save()
        users = User.objects.all()
        name_lot = post_request.get('lot').get('name')
        name_user = post_request.get('user').get('username')
        lots = Lot.objects.all().filter(name=name_lot)
        # users = User.objects.all().filter(username=name_user)
        print(users)
        if len(lots) > 0:
            print(lots)






