from django.utils import timezone
from rest_framework import permissions


class IsSupportEmployee(permissions.BasePermission):
    message = "Support employee can only read data"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.groups == 'support':
            return False
        return True


class IsEventFinish(permissions.BasePermission):
    message = "An event can't be updated once it's finished"

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.event_date > timezone.now().date()


class IsSaleEmployeeassignee(permissions.BasePermission):
    message = "Can't update an event if the employee is not assigned to it"

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.contract.client.sales_contact == request.user
