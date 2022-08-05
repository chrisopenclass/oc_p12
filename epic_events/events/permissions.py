from django.utils import timezone
from rest_framework import permissions
from django.contrib.auth.models import Group


class IsSupportEmployee(permissions.BasePermission):
    message = "Support employee can only update"

    def has_permission(self, request, view):
        if request.method == 'PUT':
            if not Group.objects.get(name="support") in request.user.groups.all():
                return False
        if request.method == 'POST':
            if not Group.objects.get(name="sales") in request.user.groups.all():
                return False
        return True


class IsEventFinish(permissions.BasePermission):
    message = "An event can't be updated once it's finished"

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if obj.event_date > timezone.now().date():
            return False

        if request.method in permissions.SAFE_METHODS:
            return True
        return True
