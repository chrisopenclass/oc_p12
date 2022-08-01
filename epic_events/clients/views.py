from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSaleEmployee
from django_filters import rest_framework as filters


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSaleEmployee]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('first_name', 'mail_adress')

    def get_queryset(self):
        return Client.objects.all()
