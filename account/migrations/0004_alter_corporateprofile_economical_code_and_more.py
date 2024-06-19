# Generated by Django 5.0.6 on 2024-06-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_address_address_line_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporateprofile',
            name='economical_code',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Economical Code'),
        ),
        migrations.AlterField(
            model_name='corporateprofile',
            name='national_code',
            field=models.BigIntegerField(unique=True, verbose_name='National Code'),
        ),
        migrations.AlterField(
            model_name='corporateprofile',
            name='phone',
            field=models.BigIntegerField(unique=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='corporateprofile',
            name='register_number',
            field=models.BigIntegerField(unique=True, verbose_name='Register Number'),
        ),
    ]
