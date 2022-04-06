from django.http import HttpResponse
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.description),
]
