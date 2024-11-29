# Generated by Django 5.1.3 on 2024-11-29 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название салона')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('latitude', models.FloatField(verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'Салон',
                'verbose_name_plural': 'Салоны',
            },
        ),
        migrations.CreateModel(
            name='SalonSocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network', models.CharField(max_length=100, verbose_name='Социальная сеть')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.salon', verbose_name='Салон')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
    ]