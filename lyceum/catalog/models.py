from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import validate_slug
from .validators import validate_text
from core.models import CustomModel, CustomModelSlug
User = get_user_model()


class Item(CustomModel):

    name = models.CharField(verbose_name='Название', max_length=150)
    text = models.TextField(verbose_name='Описание',
                            validators=[validate_text])

    tags = models.ManyToManyField(
        'Tag', verbose_name='теги', related_name='tags', blank=True)
    category = models.ForeignKey(
        'Category', verbose_name='Категория', related_name='category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Tag(CustomModelSlug):

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(CustomModelSlug):

    weight = models.PositiveSmallIntegerField(verbose_name='Вес',
                                              default=100)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
