from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def user_list(request):
    template = 'users/user_list.html'
    context = {}
    return render(request, template, context)


def user_detail(request, pk):
    template = 'users/user_detail.html'
    context = {}
    return render(request, template, context)


def signup(request):
    template = 'users/signup.html'
    context = {}
    return render(request, template, context)


def profile(request):
    template = 'users/profile.html'
    context = {}
    return render(request, template, context)
