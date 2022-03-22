from tabnanny import verbose
from unicodedata import category
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import validate_slug, MaxValueValidator, MinValueValidator
from .validators import validate_correct

User = get_user_model()


class Item(models.Model):
    id = models.PositiveIntegerField(default=1,
                                     primary_key=True, validators=[MinValueValidator(1)])
    is_published = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
    text = models.TextField(validators=[validate_correct])

    tags = models.ManyToManyField('Tag', blank=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Tag(models.Model):
    id = models.PositiveIntegerField(default=1,
                                     primary_key=True, validators=[MinValueValidator(1)])
    is_published = models.BooleanField(default=True)
    slug = models.TextField(max_length=200, unique=True,
                            validators=[validate_slug])

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.slug


class Category(models.Model):
    id = models.PositiveIntegerField(default=1,
                                     primary_key=True, validators=[MinValueValidator(1)])
    is_published = models.BooleanField(default=True)
    slug = models.TextField(max_length=200, unique=True,
                            validators=[validate_slug])
    weight = models.PositiveIntegerField(
        default=100, validators=[MinValueValidator(1), MaxValueValidator(32767)])

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
