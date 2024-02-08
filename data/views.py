from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import DataModel
from .serializers import DataSerializer
# Create your views here.

class DataList(ListAPIView):
    queryset = DataModel.objects.all()
    serializer_class = DataSerializer