from rest_framework import permissions


class IsSaleEmployee(permissions.BasePermission):
    message = "Only sales employee assigned to the client can add or update client data"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.groups == 'SUPPORT':
            return False
        return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.sales_contact == request.user
