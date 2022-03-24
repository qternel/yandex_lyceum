from django.db import models
from django.core.validators import validate_slug


class CustomModel(models.Model):
    is_published = models.BooleanField(verbose_name ='Опубликовано',default=True)
    


    class Meta:
        abstract = True

class CustomModelSlug(CustomModel):
    slug = models.TextField(verbose_name = 'Название' ,max_length=200, unique=True,
                            validators=[validate_slug])

    class Meta:
        abstract = True