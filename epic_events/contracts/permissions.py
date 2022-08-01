from rest_framework import permissions


class IsSaleEmployeeAssigned(permissions.BasePermission):
    message = "You can update a contract only if you're assigned to it"

    def has_permission(self, request, view):
        return request.user

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.client.sales_contact == request.user


class IsSupportEmployee(permissions.BasePermission):
    message = "Support employee can only read data"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.groups == 'support':
            return False
        return True
