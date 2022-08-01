from rest_framework import viewsets
from .models import Contract
from .serializers import ContractSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSaleEmployeeAssigned, IsSupportEmployee
from django_filters import rest_framework as filters


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsSaleEmployeeAssigned, IsSupportEmployee]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('client', 'date_created', 'amount')

    def get_queryset(self):
        return Contract.objects.all()
