from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['date', 'type', 'title', 'start_time', 'end_time']
    list_display_links = ['title']
    list_filter = ['type']
