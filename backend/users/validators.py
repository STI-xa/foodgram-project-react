import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            'Имя me недоступно. Выберите другое.'
        )
    if re.search(r'^[\w.@+-]+\Z', value) is None:
        unmatch_symbols = ' '.join(set(
            symbol for symbol in value if not re.match(r'^[\w.@+-]+\Z', symbol)
        ))
        raise ValidationError(
            f'Данное имя недоступно.'
            f' Недопустимые символы: {unmatch_symbols}'
        )
    return value
