# Generated by Django 5.1.3 on 2024-11-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0008_rename_otp_code_otp_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]