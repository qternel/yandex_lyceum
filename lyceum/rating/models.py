from catalog.models import Item, User
from django.db import models


class Rating(models.Model):

    EMOTION_TYPES = (
        (0, 'Оценка отсутствует'),
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь'),
    )
    star = models.IntegerField(
        verbose_name='Оценка', null=True, choices=EMOTION_TYPES)
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='user',
        on_delete=models.CASCADE,
        null=True)
    item = models.ForeignKey(Item, verbose_name='Товар', related_name='raiting',
                             on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item.name

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'
        # unique_together = [['user', 'item']]
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'item'], name='unique_rating')
        ]
