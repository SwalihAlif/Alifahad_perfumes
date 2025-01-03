# Generated by Django 5.1.3 on 2024-11-25 10:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0002_cart_total_amount_without_coupon'),
        ('coupon_app', '0001_initial'),
        ('product_app', '0005_remove_product_offer_product_product_delete_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupon_app.coupons'),
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon_active',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='coupon',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupon_app.coupons'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='coupon_active',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_app.variant')),
            ],
        ),
    ]
