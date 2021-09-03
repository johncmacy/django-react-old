from rest_framework.serializers import ModelSerializer
from .models import Thing

class ThingSerializer(ModelSerializer):
    class Meta:
        model = Thing
        fields = '__all__'