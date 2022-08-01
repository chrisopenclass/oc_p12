from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSaleEmployee


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSaleEmployee]

    def get_queryset(self):
        return Client.objects.all()
