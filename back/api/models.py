from django.db import models


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
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name="Салон")
    social_network = models.CharField(max_length=100, verbose_name="Социальная сеть")
    link = models.URLField(verbose_name="Ссылка")

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"

    def __str__(self):
        return f"{self.salon.name} - {self.social_network}"
