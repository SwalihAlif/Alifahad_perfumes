# Generated by Django 5.1.3 on 2024-11-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_profile_delete_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]