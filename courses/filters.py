import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_by_categories')

    class Meta:
        model = Course
        fields = []

    def filter_by_categories(self, queryset, name, value):
        categories = value.split(',')
        return queryset.filter(category__in=categories)
