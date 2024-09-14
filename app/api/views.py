from django.shortcuts import render
from rest_framework import viewsets

from .models import FruitFaq
from .serializers import FruitFaqSerializer


# Create your views here.

class FruitFaqViewSet(viewsets.ModelViewSet):
    queryset = FruitFaq.objects.all()
    serializer_class = FruitFaqSerializer


