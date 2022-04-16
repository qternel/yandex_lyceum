from django.db.models import Avg, Count, Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.views.generic import View
from rating.models import Rating

from catalog.forms import SelectStarForm
from catalog.models import Category, Item, Tag


def item_list(request):
    TEMPLATE = 'catalog/item_list.html'
    categories = Category.objects.published_category()
    context = {'categories': categories}
    return render(request, TEMPLATE, context)


def item_detail(request, pk):
    TEMPLATE = 'catalog/item_detail.html'
    # if request.method == 'POST':
    #     item = get_object_or_404(
    #         Item.objects.published_items(),
    #         pk=pk,
    #         is_published=True)
    item = get_object_or_404(
            Item.objects.published_items(),
            pk=pk,
            is_published=True)
    # star_form = SelectStarForm(request.POST)
    star_form = SelectStarForm(request.POST or None)
    if star_form.is_valid() and request.user.is_authenticated:
        Rating.objects.update_or_create(
            item=item, user=request.user, defaults={
                'star': star_form.cleaned_data['star']})
        return redirect('item_detail', pk)

    
    stars = item.rating.exclude(star=0).aggregate(Avg('star'), Count('star'))
    user_star = 0
    if request.user.is_authenticated:
        user_star = Rating.objects.only('star').filter(
            item=item, user=request.user).first()

    context = {'item': item, 'stars': stars,
               'user_star': user_star, 'form': SelectStarForm()}
    return render(request, TEMPLATE, context)
