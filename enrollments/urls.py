from django.urls import path
from enrollments import views

urlpatterns = [
    path('enrollments/', views.EnrollmentList.as_view()),
    path('enrollments/<int:pk>/', views.EnrollmentDetail.as_view()),
]