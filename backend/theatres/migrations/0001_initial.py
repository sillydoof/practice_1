# Generated by Django 5.1.2 on 2024-11-28 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0003_movie_trailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_number', models.CharField(max_length=10)),
                ('seat_capacity', models.PositiveIntegerField()),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='theatres.theatre')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=5)),
                ('number', models.PositiveIntegerField()),
                ('is_vip', models.BooleanField(default=False)),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='theatres.screen')),
            ],
            options={
                'unique_together': {('screen', 'row', 'number')},
            },
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='movies.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='theatres.screen')),
            ],
            options={
                'unique_together': {('screen', 'movie', 'date', 'time')},
            },
        ),
    ]