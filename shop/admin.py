from django.contrib import admin
from .models import *

class TrackAdmin(admin.ModelAdmin):
    list_display = ["track_name", "is_active"]
    list_filter = ["date"]

    class Meta:
        model = Track

admin.site.register(Track, TrackAdmin)