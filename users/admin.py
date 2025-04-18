from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     search_fields = ("name",)
#     list_filter = ("is_staff", "is_active", "is_superuser")
#     readonly_fields = ("last_login", "date_joined")


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "password",
                    "name",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = ("name",)
