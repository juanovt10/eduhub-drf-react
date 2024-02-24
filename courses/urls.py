from django.urls import path
from courses import views
from .views import CourseCategoryList

urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
    path('course-categories/', CourseCategoryList.as_view(), name='course-categories'),
]