from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Salon(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название салона")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")

    class Meta:
        verbose_name = "Салон"
        verbose_name_plural = "Салоны"

    def __str__(self):
        return self.name


class SalonSocialNetwork(models.Model):
    salon = models.ForeignKey(
        Salon, on_delete=models.CASCADE, verbose_name="Салон"
    )  # noqa
    social_network = models.CharField(
        max_length=100, verbose_name="Социальная сеть"
    )  # noqa
    link = models.URLField(verbose_name="Ссылка")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return f"{self.salon.name} - {self.social_network}"


class Slider(models.Model):
    image = models.ImageField(upload_to="slider/", verbose_name="Изображение")
    description = models.CharField(max_length=100, verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class Tags(models.Model):
    name = models.CharField(
        max_length=128, verbose_name="Название тега", unique=True
    )  # noqa

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Master(models.Model):
    salon = models.ForeignKey(
        Salon, on_delete=models.CASCADE, verbose_name="Салон"
    )  # noqa
    name = models.CharField(max_length=64, verbose_name="Имя")
    short_description = models.CharField(
        max_length=128, verbose_name="Краткое описание", blank=True, null=True
    )
    description = models.CharField(
        max_length=1024, verbose_name="Полное описание", blank=True, null=True
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        verbose_name="Рейтинг",
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ],
    )
    experience = models.IntegerField(verbose_name="Опыт работы", default=0)
    tags = models.ManyToManyField(
        Tags, verbose_name="Теги", blank=True, related_name="masters"
    )
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    image = models.ImageField(upload_to="masters/", verbose_name="Изображение")
    start_cost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость услуги"
    )

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

    def __str__(self):
        return self.name
