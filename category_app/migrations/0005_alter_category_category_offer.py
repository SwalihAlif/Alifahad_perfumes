# Generated by Django 5.1.3 on 2024-11-28 05:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0004_alter_category_category_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_offer',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
