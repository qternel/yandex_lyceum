from django.shortcuts import render

from catalog.models import Item


def home(request):
    TEMPLATE = 'homepage/home.html'
    RANDOM_ITEMS_COUNT = 3
    items = Item.objects.published_items().order_by('?')[:RANDOM_ITEMS_COUNT]
    context = {'items': items}
    return render(request, TEMPLATE, context)
