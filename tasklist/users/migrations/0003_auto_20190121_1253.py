# Generated by Django 2.1.5 on 2019-01-21 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190119_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=40, validators=[django.core.validators.EmailValidator()]),
        ),
    ]