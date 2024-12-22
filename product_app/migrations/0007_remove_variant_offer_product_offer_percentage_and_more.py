# Generated by Django 5.1.3 on 2024-11-28 05:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0006_rename_product_delete_product_delete_opt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='offer',
        ),
        migrations.AddField(
            model_name='product',
            name='offer_percentage',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='variant',
            name='offer_percentage',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]