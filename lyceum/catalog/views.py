from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag


def item_list(request):
    template = 'catalog/item_list.html'
    items = Item.objects.filter(is_published=True).prefetch_related(
        'tags').only('name', 'text', 'tags__name')
    context = {'items': items}
    return render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/item_detail.html'
    item = get_object_or_404(
        Item.objects.select_related('category').prefetch_related(
            Prefetch(
                'tags',
                queryset=Tag.objects.filter(
                    is_published=True))).only(
            'name',
            'text',
            'category',
            'tags__name'),
        pk=pk)
    context = {'item': item}
    return render(request, template, context)
