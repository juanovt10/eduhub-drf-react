from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('title', 'owner', 'created_at')
    search_fields = ['title', 'owner', 'category']
    list_filter = ('category', 'owner')
    