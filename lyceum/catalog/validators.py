from django.forms import ValidationError


def validate_text(value):
    word_list = {'Превосходно', 'Роскошно'}
    if len(value.split()) < 2:
        raise ValidationError('В строке должно быть минимум 2 слова')

    if not any(filter(lambda x: x.lower() in value.lower(), word_list)):
        raise ValidationError(f'Используйте в описании слова {word_list}')
