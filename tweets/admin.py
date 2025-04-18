from django.contrib import admin

from .models import Like, Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("payload", "get_user_name")

    def get_user_name(self, obj):
        return obj.user.name

    get_user_name.short_description = "User"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("tweet", "get_user_name")

    def get_user_name(self, obj):
        return obj.user.name

    get_user_name.short_description = "User"
