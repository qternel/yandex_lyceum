from catalog.models import Item
from django.shortcuts import render


def home(request):
    TEMPLATE = 'homepage/home.html'
    RANDOM_ITEMS_COUNT = 3
    items = Item.objects.published_items().order_by('?')[:RANDOM_ITEMS_COUNT]
    context = {'items': items}
    return render(request, TEMPLATE, context)
