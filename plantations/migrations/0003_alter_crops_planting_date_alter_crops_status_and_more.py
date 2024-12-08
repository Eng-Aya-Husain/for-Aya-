# Generated by Django 5.1.3 on 2024-12-01 18:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantations', '0002_alter_areaseason_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crops',
            name='planting_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='crops',
            name='status',
            field=models.CharField(choices=[('qrowing', 'ينمو'), ('harvested', 'تم الحصاد'), ('failed', 'تالف')], default='growing', max_length=255),
        ),
        migrations.AlterField(
            model_name='plants',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='plantations.categories'),
        ),
    ]