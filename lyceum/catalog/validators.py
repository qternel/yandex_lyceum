from django.forms import ValidationError

def validate_correct(value):
    word_list = {'превосходно', 'роскошно'}
    text = set(value.lower().split())
    difference = word_list - text #множество, состоящее из разницы
    if len(difference) == len(word_list):
        raise ValidationError(f'Необходимо использовать слова : {word_list}')
    
    if len(text) < 2:
        raise ValidationError('Необходимо использовать минимум 2 слова.')