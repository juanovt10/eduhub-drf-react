from django.contrib import admin
from .models import Rating

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ('owner', 'created_at')
    search_fields = ['owner', 'course']
    list_filter = ('owner', 'course')
