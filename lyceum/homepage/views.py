from django.shortcuts import render

from catalog.models import Item


def home(request):
    template = 'homepage/home.html'
    random_items_count = 3
    items = Item.objects.filter(
        is_published=True).prefetch_related('tags').only(
        'name', 'text', 'tags__name').order_by('?')[
            :random_items_count]
    context = {'items': items}
    return render(request, template, context)
