from django.contrib import admin
from .models import Rating

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ('title', 'owner', 'created_at')
    search_fields = ['title', 'owner', 'course']
    list_filter = ('title', 'owner', 'course')
