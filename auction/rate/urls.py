from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('lots', views.LotActiveList.as_view(), name='lots'),
]
