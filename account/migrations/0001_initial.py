# Generated by Django 5.0.6 on 2024-06-17 09:53

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
            name='CorporateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('national_code', models.CharField(max_length=10, unique=True, verbose_name='National Code')),
                ('register_number', models.CharField(max_length=50, unique=True, verbose_name='Register Number')),
                ('economical_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Economical Code')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Phone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Corporate Profile',
                'verbose_name_plural': 'Corporate Profiles',
                'db_table': 'customer_corprofile',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('national_code', models.CharField(max_length=10, unique=True, verbose_name='National Code')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6, verbose_name='Gender')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Phone')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('job', models.CharField(blank=True, max_length=50, null=True, verbose_name='Job')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Personal Profile',
                'verbose_name_plural': 'Personal Profiles',
                'db_table': 'customer_perprofile',
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 2')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('zip_code', models.CharField(max_length=10, verbose_name='ZIP Code')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('corporate_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.corporateprofile', verbose_name='Corporate Profile')),
                ('personal_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.personalprofile', verbose_name='Personal Profile')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'customer_address',
                'ordering': ['city', 'state'],
            },
        ),
    ]
