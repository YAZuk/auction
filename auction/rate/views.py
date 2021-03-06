from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import LotSerializer, RateSerializer
from .models import Lot, Rate, WinnerLot
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.


def index(request):
        """
        :param request:
        :return:
        """
        # model = Rate
        # queryset = Rate.objects.all()

        latest_rate = Rate.objects.order_by('-pub_date')
        return HttpResponse(latest_rate)


class LotActiveList(generics.ListCreateAPIView):
    """
    """
    model = Lot
    serializer_class = LotSerializer
    queryset = Lot.objects.filter(status="OPEN")
    permission_classes = [permissions.IsAuthenticated]


class CreateRate(generics.ListCreateAPIView):
    """
    """
    model = Rate
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid:
            lot_request = Lot.objects.filter(name=self.request.data['lot.name'])
            price_request = self.request.data['price']
            if len(lot_request) == 1:
                serializer.save(user=self.request.user, lot=lot_request[0], price=price_request)

    def get_queryset(self):
        return Rate.objects.filter(user=self.request.user)
