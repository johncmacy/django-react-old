from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Thing
from .serializers import ThingSerializer

class ThingViewSet(ModelViewSet):
    model = Thing
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
