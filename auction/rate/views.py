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
        latest_rate = Rate.objects.order_by('-pub_date')
        # output = ', '.join([q.price for q in latest_rate])
        return HttpResponse(latest_rate)


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
        serializer.save()
        if self.request.user.is_authenticated:
            # post_request.get('lot').get('name')
            name_user = User.objects.filter(username=self.request.user)
            print(name_user, Lot.objects.filter(name=self.request.data['lot.name']), self.request.data['price'])







