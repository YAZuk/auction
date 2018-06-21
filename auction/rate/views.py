from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import LotSerializer, RateSerializer
from .models import Lot, Rate, WinnerLot

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
        # users = Rate.user.objects.all()
        name_lot = post_request.get('lot').get('name')
        lots = Lot.objects.all().filter(name=name_lot)
        if len(lots) > 0:
            print(lots)






