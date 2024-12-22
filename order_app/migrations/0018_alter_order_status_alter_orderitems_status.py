# Generated by Django 5.1.3 on 2024-12-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0017_rename_cancel_return_confirm_orderitems_item_return_requested_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Order Pending'), ('Processing', 'Processing'), ('Confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], default='Pending'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='status',
            field=models.CharField(choices=[('Pending', 'Order Pending'), ('Processing', 'Processing'), ('Confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], default='Pending', max_length=255),
        ),
    ]
