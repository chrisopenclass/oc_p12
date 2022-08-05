from rest_framework.serializers import ModelSerializer
from clients.models import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ["id",
                  "first_name",
                  "last_name",
                  "mail_adress",
                  "phone",
                  "mobile",
                  "company_name",
                  "date_created",
                  "date_edited",
                  "sales_contact",
                  "is_customer"
                  ]
        read_only_fields = ['sales_contact']
