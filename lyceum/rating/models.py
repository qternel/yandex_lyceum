from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator
from django.forms import IntegerField
from django.contrib.auth import get_user_model
from catalog.models import Item
from catalog.models import User
# User = get_user_model()


class Rating(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True, validators=[MinValueValidator(1)])
    EMOTION_TYPES = (
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь'),
    )
    star = models.IntegerField(null=True, choices=EMOTION_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'
        unique_together = [['user', 'item']]
