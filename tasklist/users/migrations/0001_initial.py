# Generated by Django 2.1.5 on 2019-01-19 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.AutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')
                ),
                (
                    'name',
                    models.CharField(max_length=50)
                ),
                (
                    'email',
                    models.CharField(max_length=30)
                ),
                (
                    'age',
                    models.CharField(max_length=2)
                ),
                (
                    'user_type',
                    models.CharField(max_length=7)
                ),
                    ],
        ),
    ]
