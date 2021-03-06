# Generated by Django 3.0.8 on 2020-08-06 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('number_of_seats', models.DecimalField(decimal_places=0, max_digits=2)),
                ('remaining_seats', models.DecimalField(decimal_places=0, max_digits=2)),
                ('bus_fare', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('departure_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=2)),
                ('date_booked', models.DateField(default=django.utils.timezone.now)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bus_booked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booker.Bus')),
            ],
        ),
    ]
