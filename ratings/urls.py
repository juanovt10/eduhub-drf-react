from django.urls import path
from ratings import views

urlpatterns = [
    path('ratings/', views.RatingList.as_view()),
    path('ratings/<int:pk>/', views.RatingDetail.as_view()),
    path(
        'ratings/stats/<int:course_id>/', views.RatingStatsView.as_view()
    )
]