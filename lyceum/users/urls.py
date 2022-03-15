from django.urls import path
from . import views

urlpatterns = [
    path('auth/users/', views.user_list),
    path('auth/users/<int:pk>/', views.user_detail),
    path('auth/signup/', views.signup),
    path('auth/profile/', views.profile)
]
