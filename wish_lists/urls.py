from django.urls import path
from wish_lists import views

urlpatterns = [
    path('wish_lists/', views.WishListList.as_view()),
    path('wish_lists/<int:pk>/', views.WishListDetail.as_view()),
]