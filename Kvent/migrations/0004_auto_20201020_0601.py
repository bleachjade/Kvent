# Generated by Django 3.1.2 on 2020-10-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kvent', '0003_auto_20201020_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date_time',
        ),
        migrations.AddField(
            model_name='event',
            name='full',
            field=models.BooleanField(default=False),
        ),
    ]
