from django.core.exceptions import ValidationError


def at_least_3(string):
    if len(string) < 3:
        raise ValidationError('Too shoooort, chert')