from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('catalog/', views.item_list),
    path('catalog/<int:pk>/', views.item_detail),
]
