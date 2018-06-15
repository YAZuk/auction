from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import LotSerializer
from .models import Lot, Rate, WinnerLot

# Create your views here.


def index(request):
    return HttpResponse("Index rate")


class LotActiveList(generics.ListCreateAPIView):
    """
    """
    model = Lot
    serializer_class = LotSerializer
    queryset = []







