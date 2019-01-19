from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30) ## EmailValidator
    age = models.CharField(max_length=2) ## Min 18
    user_type = models.CharField(max_length=7) ## Choices [admin, manager, default]
