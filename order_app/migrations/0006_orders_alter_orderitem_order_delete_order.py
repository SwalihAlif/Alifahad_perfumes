# Generated by Django 5.1.3 on 2024-11-25 14:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0005_rename_ordered_at_order_order_date_and_more'),
        ('user_profile_app', '0004_alter_userprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('serial_number', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('payment_method', models.CharField(max_length=20, null=True)),
                ('payment_online_id', models.CharField(blank=True, default='0000', max_length=50, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('coupon_name', models.CharField(blank=True, max_length=50, null=True)),
                ('coupon_discount', models.CharField(blank=True, max_length=50, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_set', to='user_profile_app.userprofile')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order_app.orders'),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
