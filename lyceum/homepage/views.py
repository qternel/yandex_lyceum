from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    template = 'homepage/home.html'
    context = {}
    return render(request, template, context)
