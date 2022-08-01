from django.contrib import admin
from user.models import Users
from django.contrib.auth.admin import UserAdmin


admin.site.empty_value_display = '(None)'


class UserStaff(UserAdmin):
    model = Users
    list_display = ("last_name", "first_name")
    list_filter = ("groups__name",)


admin.site.register(Users, UserStaff)
