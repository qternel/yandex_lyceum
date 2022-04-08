from django.db.models import Prefetch
from django.shortcuts import render

from catalog.models import Item, Tag


def home(request):
    template = 'homepage/home.html'
    random_items_count = 3
    items = Item.objects.filter(
        is_published=True).prefetch_related(
        Prefetch(
            'tags',
            queryset=Tag.objects.filter(
                is_published=True))).order_by('?')[:random_items_count]
    context = {'items': items}
    return render(request, template, context)
