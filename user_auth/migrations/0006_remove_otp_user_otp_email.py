# Generated by Django 5.1.3 on 2024-11-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_alter_otp_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='user',
        ),
        migrations.AddField(
            model_name='otp',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]