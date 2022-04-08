from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag


def item_list(request):
    TEMPLATE = 'catalog/item_list.html'
    items = Item.objects.filter(
        is_published=True).prefetch_related(
        Prefetch('tags',
                 queryset=Tag.objects.filter(
                     is_published=True).only("name")))
    context = {'items': items}
    return render(request, TEMPLATE, context)


def item_detail(request, pk):
    TEMPLATE = 'catalog/item_detail.html'
    item = get_object_or_404(
        Item.objects.select_related('category').only(
            'name',
            'text',
            'category__name',
            'tags__name').prefetch_related(
            Prefetch(
                'tags',
                queryset=Tag.objects.filter(
                    is_published=True).only('name'))),
        pk=pk,
        is_published=True)

    context = {'item': item}
    return render(request, TEMPLATE, context)
