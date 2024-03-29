import django_filters
from .models import Course


class CourseFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_by_categories')
    has_videos = django_filters.CharFilter(method='filter_has_videos')
    has_articles = django_filters.CharFilter(method='filter_has_articles')
    has_tests = django_filters.CharFilter(method='filter_has_tests')
    min_rating = django_filters.NumberFilter(
        field_name='overall_rating', lookup_expr='gte'
    )
    enrolled = django_filters.BooleanFilter(method='filter_enrolled')
    wish_listed = django_filters.BooleanFilter(method='filter_wish_listed')
    owner_username = django_filters.CharFilter(
        method='filter_by_owner_username'
    )

    class Meta:
        model = Course
        fields = []

    def filter_by_categories(self, queryset, name, value):
        categories = value.split(',')
        return queryset.filter(category__in=categories)

    def filter_has_videos(self, queryset, name, value):
        if value:
            return queryset.filter(video_hours__gt=0)
        return queryset

    def filter_has_articles(self, queryset, name, value):
        if value:
            return queryset.filter(article_count__gt=0)
        return queryset

    def filter_has_tests(self, queryset, name, value):
        if value:
            return queryset.filter(test_count__gt=0)
        return queryset

    def filter_enrolled(self, queryset, name, value):
        if self.request:
            if value:
                enrolled_course_ids = self.request.user.enrollment_set.values_list(
                    'course_id', flat=True
                )
                queryset = queryset.filter(id__in=enrolled_course_ids)
        return queryset

    def filter_wish_listed(self, queryset, name, value):
        if self.request:
            if value:
                wish_listed_course_ids = self.request.user.wishlist_set.values_list(
                    'course_id', flat=True
                )
                queryset = queryset.filter(id__in=wish_listed_course_ids)
        return queryset

    def filter_by_owner_username(self, queryset, name, value):
        return queryset.filter(owner__username=value)

        return queryset
        