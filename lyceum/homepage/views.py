from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from http import HTTPStatus
# Create your views here.


def home(request):
    return HttpResponse('Главная')
