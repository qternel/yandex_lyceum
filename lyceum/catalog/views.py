from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from catalog.models import Item, Tag
from django.db.models import Prefetch


def item_list(request):
    template = 'catalog/item_list.html'
    items = Item.objects.filter(is_published=True)
    context = {'items': items}
    return render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/item_detail.html'
    item = get_object_or_404(Item.objects.select_related('category').prefetch_related(Prefetch('tags', queryset=Tag.objects.filter(is_published=True))), pk=pk)
    context = {'item': item}
    return render(request, template, context)
