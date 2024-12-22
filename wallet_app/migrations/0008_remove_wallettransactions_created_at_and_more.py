# Generated by Django 5.1.3 on 2024-12-11 06:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0007_alter_spinhistory_is_won_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallettransactions',
            name='created_at',
        ),
        migrations.AddField(
            model_name='wallettransactions',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='wallettransactions',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wallettransactions',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='wallettransactions',
            name='transaction_type',
            field=models.CharField(choices=[('spent', 'Spent'), ('earned', 'Earned'), ('refund', 'Refund')], max_length=7, null=True),
        ),
    ]