# Generated by Django 3.1.1 on 2020-12-03 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kvent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(default='https://storage.googleapis.com/kvent_bucket/upload/no_img.png', null=True, upload_to='upload/'),
        ),
    ]
