from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, pk):
    return HttpResponse('Подробно элемент')
