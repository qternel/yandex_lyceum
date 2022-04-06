from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def description(request):
    template = 'about/description.html'
    context = {}
    return render(request, template, context)
