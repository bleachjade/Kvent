# Generated by Django 3.1.2 on 2020-10-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField(default='', max_length=50, verbose_name='Event Name')),
                ('location', models.TextField(default='', max_length=80, verbose_name='Location')),
                ('description', models.TextField(default='', max_length=100, verbose_name='Description')),
                ('number_people', models.IntegerField(default=2, verbose_name='Number of people')),
                ('date_time', models.TextField(default='2020-10-17 06:27:22', verbose_name='Date and Time')),
            ],
        ),
    ]
