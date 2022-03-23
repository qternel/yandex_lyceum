from django.db import models
from django.core.validators import validate_slug


class CustomModel(models.Model):
    is_published = models.BooleanField(default=True)
    slug = models.TextField(max_length=200, unique=True,
                            validators=[validate_slug])

    def __str__(self):
        return self.slug

    class Meta:
        abstract = True
