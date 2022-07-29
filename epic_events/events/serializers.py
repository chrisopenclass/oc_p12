from rest_framework.serializers import ModelSerializer

from .models import Event


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ["name",
                  "contract",
                  "date_created",
                  "updated_date",
                  "support_contact",
                  "attendees",
                  "event_date",
                  "notes",
                  "ended"
                  ]
