from core.models import CustomModel, CustomModelSlug
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Prefetch

from .validators import validate_text

User = get_user_model()


class CategoryManager(models.Manager):
    def published_category(self):
        return self.filter(is_published=True).prefetch_related(
            Prefetch('items', queryset=Item.objects.published_items())
        ).only('name').order_by('weight')


class ItemManager(models.Manager):
    def published_items(self):
        return self.select_related('category').only(
            'name',
            'text',
            'category__name',
            'tags__name').prefetch_related(
            Prefetch(
                'tags',
                queryset=Tag.objects.filter(
                    is_published=True).only('name')))


class TagManager(models.Manager):
    def published_tags(self):
        return self.filter(is_published=True).only('name')


class Item(CustomModel):
    name = models.CharField(verbose_name='Название', max_length=150)
    text = models.TextField(verbose_name='Описание',
                            validators=[validate_text])

    tags = models.ManyToManyField(
        'Tag', verbose_name='теги', related_name='items', blank=True)
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        related_name='items',
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    objects = ItemManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Tag(CustomModelSlug):

    objects = TagManager()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(CustomModelSlug):

    weight = models.PositiveSmallIntegerField(verbose_name='Вес',
                                              default=100)
    objects = CategoryManager()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
