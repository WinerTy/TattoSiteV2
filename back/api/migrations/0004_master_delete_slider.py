# Generated by Django 5.1.3 on 2024-11-29 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_slider_options_delete_currentsalon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('image', models.ImageField(upload_to='masters/', verbose_name='Изображение')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.salon', verbose_name='Салон')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
