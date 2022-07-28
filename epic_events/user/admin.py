from django.contrib import admin
from user.models import Users
from django.contrib.auth.admin import UserAdmin


admin.site.empty_value_display = '(None)'


class UserStaff(UserAdmin):
    model = Users
    list_display = ("last_name", "first_name", "role")
    list_filter = ("role", )
    """fields = (("first_name", "last_name"), "email", "role", "password",
              "is_active", "is_staff", "username")"""


admin.site.register(Users, UserStaff)
