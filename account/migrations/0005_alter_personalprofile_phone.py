# Generated by Django 5.0.6 on 2024-06-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_corporateprofile_economical_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalprofile',
            name='phone',
            field=models.BigIntegerField(unique=True, verbose_name='Phone'),
        ),
    ]