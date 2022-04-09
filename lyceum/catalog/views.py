from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Item


def item_list(request):
    TEMPLATE = 'catalog/item_list.html'
    categories = Category.objects.published_category()
    context = {'categories': categories}
    return render(request, TEMPLATE, context)


def item_detail(request, pk):
    TEMPLATE = 'catalog/item_detail.html'
    item = get_object_or_404(
        Item.objects.published_items(),
        pk=pk,
        is_published=True)

    context = {'item': item}
    return render(request, TEMPLATE, context)
