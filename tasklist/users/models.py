from django.db import models
from django.core.validators import validate_email, MinValueValidator


class User(models.Model):
    USER_TYPES = (
        (
            'admin',
            'admin'
        ),
        (
            'manager',
            'manager'
        ),
        (
            'default',
            'default'
        ),
    )

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40, validators=[validate_email])
    age = models.IntegerField(validators=[MinValueValidator(18)])
    user_type = models.CharField(
        max_length=7,
        choices=USER_TYPES,
        default='default'
    )
