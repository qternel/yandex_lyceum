from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item


def home(request):
    template = 'homepage/home.html'
    items = Item.objects.filter(
        is_published=True).prefetch_related('tags').only('name', 'text', 'tags').order_by('?')[0:3]
    context = {'items': items}
    return render(request, template, context)
