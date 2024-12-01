import random
from django.core.management.base import BaseCommand
from api.models import Tags, Salon, Master

tattoo_categories = [
    "Классические",
    "Оригинальные",
    "Минималистичные",
    "Тематические",
    "Анималистические",
    "Геометрические",
    "Биомеханические",
    "Трафаретные",
    "Пермаментные",
    "Черно-белые",
    "Цветные",
    "Надписи",
    "Портреты",
    "Флора",
    "Фауна",
    "Мифология",
    "Культура",
    "Искусство",
    "Пиктограммы",
    "Символы",
    "Абстрактные",
    "Стилизация",
    "Графика",
    "Скульптура",
    "Архитектура",
    "Музыка",
    "Спорт",
    "Техника",
    "Наука",
    "История",
    "Фантастика",
    "Фэнтези",
    "Комиксы",
    "Манга",
    "Аниме",
    "Игры",
    "Кино",
    "Литература",
    "Музыкальные группы",
    "Личности",
    "Символика",
    "Религия",
]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--salon_id", type=int, help="Salon ID")

    def handle(self, *args, **options):
        salon_id = options["salon_id"]

        if salon_id:
            self.create_tag_for_master(salon_id)
        else:
            self.stdout.write(self.style.ERROR("Salon ID is required"))

    def create_tags(self):
        for category in tattoo_categories:
            Tags.objects.get_or_create(name=category)

    def create_tag_for_master(self, salon_id):
        salon = Salon.objects.filter(id=salon_id).first()
        if not salon:
            self.stdout.write(self.style.ERROR("Salon not found"))
            return

        masters = Master.objects.filter(salon=salon)
        if not masters:
            self.stdout.write(self.style.ERROR("No masters found"))
            return
        tags = Tags.objects.all()
        if not tags:
            tags = self.create_tags()
        for master in masters:
            random_tags = random.sample(list(tags), random.randint(1, 6))
            master.tags.add(*random_tags)
            master.save()
