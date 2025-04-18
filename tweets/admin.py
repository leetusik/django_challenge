from django.contrib import admin

from .models import Like, Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("content", "user")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("tweet", "user")
