# Generated by Django 5.1.3 on 2024-12-11 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0015_alter_order_coupon_discount_alter_order_coupon_name_and_more'),
        ('wallet_app', '0008_remove_wallettransactions_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallettransactions',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_app.order'),
        ),
        migrations.AlterField(
            model_name='wallettransactions',
            name='transaction_type',
            field=models.CharField(choices=[('spent', 'Spent'), ('earned', 'Earned'), ('refund', 'Refund'), ('spin', 'Spin Reward')], max_length=7, null=True),
        ),
    ]
