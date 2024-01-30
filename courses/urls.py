from django.urls import path
from courses import views

urlpatterns = [
    path('courses/', views.CourseList.as_view()),
]