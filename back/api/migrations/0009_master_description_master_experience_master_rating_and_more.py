# Generated by Django 5.1.3 on 2024-12-01 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_salon_name_salon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Полное описание'),
        ),
        migrations.AddField(
            model_name='master',
            name='experience',
            field=models.IntegerField(default=0, verbose_name='Опыт работы'),
        ),
        migrations.AddField(
            model_name='master',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='master',
            name='short_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='master',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
    ]
