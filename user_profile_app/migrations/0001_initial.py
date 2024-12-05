# Generated by Django 5.1.3 on 2024-11-19 14:58

import cloudinary.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_code', models.CharField(max_length=160, unique=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_address', models.BooleanField(default=False)),
                ('full_name', models.CharField(default='to add', max_length=50)),
                ('landmark', models.CharField(blank=True, max_length=30, null=True)),
                ('address_type', models.CharField(default='Home', max_length=10)),
                ('accessible', models.CharField(default='Not Added', max_length=50)),
                ('area', models.CharField(default='Not Added', max_length=50)),
                ('city', models.CharField(default='Not Added', max_length=50)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message="Pincode must be 6 'digits'", regex='^\\d{6}$')])),
                ('post_office', models.CharField(default='Not Added', max_length=40)),
                ('state', models.CharField(default='Not Added', max_length=40)),
                ('phone_no', models.CharField(default='00000000', max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be 10 'digits'", regex='^\\d{10}$')])),
                ('alternative_phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be 10 'digits'", regex='^\\d{10}$')])),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='Image must be a valid file type: .jpg, .jpeg, .png, or .webp', regex='^.*\\.(jpg|jpeg|png|webp)$')], verbose_name='image')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
