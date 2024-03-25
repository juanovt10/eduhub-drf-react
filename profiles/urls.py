from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('instructor_apply/', views.InstructorApplicationCreateView.as_view(), name='instructor_application')
]