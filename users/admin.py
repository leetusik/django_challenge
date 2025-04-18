from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("is_staff", "is_active", "is_superuser")
    readonly_fields = ("last_login", "date_joined")
