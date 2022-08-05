from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSaleEmployee
from django_filters import rest_framework as filters
from events.models import Event
from contracts.models import Contract
from django.contrib.auth.models import Group


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsSaleEmployee]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('first_name', 'mail_adress')

    def get_queryset(self):
        if Group.objects.get(name="support") in self.request.user.groups.all():
            list_event_of_user = []
            for event in Event.objects.filter(support_contact=self.request.user.id)\
                    .values_list('contract'):
                list_event_of_user.append(event[0])
            list_client_of_user = []
            for event in list_event_of_user:
                client = Contract.objects.filter(id=event).values_list('client')
                list_client_of_user.append(client[0][0])
                client = []
            for client_id in list_client_of_user:
                client.append(int(client_id))
            print(client)
            return Client.objects.filter(id__in=client)
        return Client.objects.filter(sales_contact=self.request.user.id)
