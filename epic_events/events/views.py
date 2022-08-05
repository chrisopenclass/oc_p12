from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsEventFinish, IsSupportEmployee
from django_filters.rest_framework import DjangoFilterBackend


class EventViewSet(viewsets.ModelViewSet):

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated,
                          IsEventFinish,
                          IsSupportEmployee]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['contract', 'event_date', 'contract__client__mail_adress',
                        'contract__client__first_name']

    def get_queryset(self):
        return Event.objects.filter(
            support_contact=self.request.user.id)
