from rest_framework import viewsets
from .models import Contract
from .serializers import ContractSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSaleEmployeeAssigned, IsSupportEmployee
from django_filters.rest_framework import DjangoFilterBackend


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsSaleEmployeeAssigned, IsSupportEmployee]

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['client__mail_adress', 'date_created', 'amount', 'client__first_name']

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    def get_queryset(self):
        return Contract.objects.filter(
            sales_contact=self.request.user.id)
