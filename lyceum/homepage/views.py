from django.db.models import Prefetch
from django.shortcuts import render

from catalog.models import Item, Tag


def home(request):
    TEMPLATE = 'homepage/home.html'
    RANDOM_ITEMS_COUNT = 3
    items = Item.objects.filter(
        is_published=True).prefetch_related(
        Prefetch(
            'tags',
            queryset=Tag.objects.filter(
                is_published=True))).order_by('?')[:RANDOM_ITEMS_COUNT]
    context = {'items': items}
    return render(request, TEMPLATE, context)
