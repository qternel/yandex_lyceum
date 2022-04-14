from django import forms
from django.forms import ChoiceField
from rating.models import Rating


class SelectStarForm(forms.Form):
    star = ChoiceField(choices=Rating.EMOTION_TYPES)
