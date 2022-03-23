from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import validate_slug, MaxValueValidator, MinValueValidator
from .validators import validate_text
from core.models import CustomModel
User = get_user_model()


class Item(models.Model):

    is_published = models.BooleanField(
        verbose_name='Опубликовано', default=True)
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


class Tag(CustomModel):

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(CustomModel):

    weight = models.PositiveIntegerField(
        default=100, validators=[MinValueValidator(1), MaxValueValidator(32767)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
