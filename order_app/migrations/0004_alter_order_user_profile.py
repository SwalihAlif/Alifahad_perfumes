# Generated by Django 5.1.3 on 2024-11-25 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0003_rename_created_at_order_ordered_at_and_more'),
        ('user_profile_app', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_set', to='user_profile_app.userprofile'),
        ),
    ]
