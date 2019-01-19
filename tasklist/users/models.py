from django.db import models
from django.core.validators import EmailValidator, MinValueValidator

class User(models.Model):
    USER_TYPES = (
        ('admin','admin'),
        ('manager','manager'),
        ('default','default'),
    )

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30, validators=[EmailValidator])
    age = models.IntegerField(validators=[MinValueValidator(18)])
    user_type = models.CharField(max_length=7, choices=USER_TYPES, default='default')
