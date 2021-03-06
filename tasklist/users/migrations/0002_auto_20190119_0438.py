# Generated by Django 2.1.5 on 2019-01-19 04:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(18)]
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(
                max_length=30,
                validators=[django.core.validators.EmailValidator]
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(
                choices=[
                    ('admin', 'admin'),
                    ('manager', 'manager'),
                    ('default', 'default')
                ],
                default='default',
                max_length=7
            ),
        ),
    ]
