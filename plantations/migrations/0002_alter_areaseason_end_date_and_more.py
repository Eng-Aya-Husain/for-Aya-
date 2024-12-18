# Generated by Django 5.1.3 on 2024-11-27 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaseason',
            name='end_date',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex='^\\d{2}-\\d{2}$')]),
        ),
        migrations.AlterField(
            model_name='areaseason',
            name='start_date',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex='^\\d{2}-\\d{2}$')]),
        ),
    ]
