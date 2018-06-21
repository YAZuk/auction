from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('activelots', views.LotActiveList.as_view(), name='activelots'),
    path('createrate', views.CreateRate.as_view(), name='createrate'),
]
