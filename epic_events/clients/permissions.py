from rest_framework import permissions
from django.contrib.auth.models import Group


class IsSaleEmployee(permissions.BasePermission):
    message = "Only sales employee assigned to the client can add or update client data"

    def has_permission(self, request, view):
        if request.method == 'POST':
            if not Group.objects.get(name="sales") in request.user.groups.all():
                return False
        return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.sales_contact == request.user
