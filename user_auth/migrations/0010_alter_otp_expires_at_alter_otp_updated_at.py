# Generated by Django 5.1.3 on 2024-11-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0009_alter_profile_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='expires_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='otp',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]