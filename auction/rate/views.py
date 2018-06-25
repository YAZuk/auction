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
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # serializer.save()

        user_auth = None
        lot_request = None

        # защита 80 левела
        users = User.objects.filter(username=self.request.user)
        if len(users) == 1:
            user_auth = users[0]

        # защита 80 левела
        lots = Lot.objects.filter(name=self.request.data['lot.name'])
        if len(lots) == 1:
            lot_request = lots[0]
        price_request = self.request.data['price']

        if (user_auth != None) and (lot_request != None):
            print(user_auth, lot_request, price_request)
            Rate.objects.create(user=user_auth, lot=lot_request, price=price_request)
            # return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)








