# Generated by Django 5.1.3 on 2024-12-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0016_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitems',
            old_name='cancel_return_confirm',
            new_name='item_return_requested',
        ),
        migrations.AddField(
            model_name='order',
            name='order_return_requested',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Pompleted', 'Completed'), ('Failed', 'Failed'), ('Refunded', 'Refunded')], default='pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='status',
            field=models.CharField(choices=[('Pending', 'Order Pending'), ('Processing', 'Processing'), ('Confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], default='Order Pending', max_length=255),
        ),
    ]