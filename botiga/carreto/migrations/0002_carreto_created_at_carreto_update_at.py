# Generated by Django 5.0.4 on 2024-05-09 16:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreto',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='carreto',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
