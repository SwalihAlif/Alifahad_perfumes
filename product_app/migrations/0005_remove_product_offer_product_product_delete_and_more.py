# Generated by Django 5.1.3 on 2024-11-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_remove_variant_offer_product_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='offer',
        ),
        migrations.AddField(
            model_name='product',
            name='product_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='variant',
            name='delete_opt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='variant',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='variant',
            name='offer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='variant',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
