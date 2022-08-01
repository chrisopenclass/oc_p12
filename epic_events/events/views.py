from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsEventFinish, IsSaleEmployeeassignee, IsSupportEmployee
from django_filters import rest_framework as filters


class EventViewSet(viewsets.ModelViewSet):

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated,
                          IsEventFinish,
                          IsSaleEmployeeassignee,
                          IsSupportEmployee]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contract', 'event_date')

    def get_queryset(self):
        return Event.objects.all()
