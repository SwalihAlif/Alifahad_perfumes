# Generated by Django 5.1.3 on 2024-11-29 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0004_rename_user_id_cart_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='user_id',
        ),
    ]
