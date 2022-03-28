from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def item_list(request):
    template = 'catalog/item_list.html'
    context = {}
    return render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/item_detail.html'
    context = {}
    return render(request, template, context)
