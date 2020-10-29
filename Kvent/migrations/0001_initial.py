from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.CharField(default='NOT SET', max_length=10, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('address', models.CharField(default='NOT SET', max_length=125, verbose_name='Address')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField(default='', max_length=50, verbose_name='Event Name')),
                ('location', models.TextField(default='', max_length=80, verbose_name='Location')),
                ('short_description', models.TextField(default='', max_length=100, verbose_name='Short Description')),
                ('long_description', models.TextField(default='', max_length=255, verbose_name='Long Description')),
                ('number_people', models.IntegerField(default=2, verbose_name='Number of people')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time')),
                ('full', models.BooleanField(default=False)),
                ('participants', models.ManyToManyField(to='Kvent.Info')),
            ],
        ),
    ]
