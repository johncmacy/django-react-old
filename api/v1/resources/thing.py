from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import Thing

class ThingSerializer(ModelSerializer):
    class Meta:
        model = Thing
        fields = '__all__'

class ThingViewSet(ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     # GET (with pk)
    #     return super().retrieve(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     # GET (many items)
    #     return super().list(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     # POST
    #     return super().create(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     # PUT
    #     return super().update(request, *args, **kwargs)

    # def partial_update(self, request, *args, **kwargs):
    #     # PATCH
    #     return super().partial_update(request, *args, **kwargs)