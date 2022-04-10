from django.core.validators import validate_slug
from django.db import models


class CustomModel(models.Model):
    is_published = models.BooleanField(
        verbose_name='Опубликовано', default=True)

    class Meta:
        abstract = True


class CustomModelSlug(CustomModel):
    name = models.CharField(verbose_name='Название',
                            max_length=150, default='')
    slug = models.TextField(verbose_name='Слаг', max_length=200,
                            unique=True,
                            validators=[validate_slug])

    class Meta:
        abstract = True
