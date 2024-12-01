from django.core.management.base import BaseCommand
from api.models import Master, Salon
import random
from decimal import Decimal
import os
from django.conf import settings
from shutil import copy2

texts = [
    "Стиль этого тату-мастера – это не просто картинка на коже, а настоящая история, которую он умело рассказывает через свои работы.",  # noqa
    "Этот тату-мастер – настоящий мастер своего дела, который уделяет внимание каждой детали. Его татуировки – это настоящие шедевры, которые поражают своей красотой и точностью исполнения.",  # noqa
    "Для этого тату-мастера татуировки – это не просто работа, а смысл жизни. Он живет и дышит тату, и это чувствуется в каждой его работе.",  # noqa
    "Этот тату-мастер создает не просто татуировки, а настоящие истории, которые заставляют задуматься и чувствовать. Его работы – это не просто рисунки на коже, а настоящие произведения искусства.",  # noqa
    "Для этого тату-мастера татуировки – это способ выразить себя, свои мысли и чувства. Он создает татуировки, которые отражают индивидуальность и свободу.",  # noqa
    "Этот тату-мастер считает, что татуировки – это настоящее искусство, которое может передать любые эмоции и чувства. Он создает татуировки, которые поражают своей красотой и глубиной.",  # noqa
    "Тату – это язык тела для этого мастера. Он создает татуировки, которые отражают индивидуальность и свободу. Его работы – это не просто рисунки на коже, а настоящие произведения искусства.",  # noqa
    "Тату – это история для этого мастера. Он создает татуировки, которые заставляют задуматься и чувствовать. Его работы – это не просто рисунки на коже, а настоящие произведения искусства.",  # noqa
    "Тату – это жизнь для этого мастера. Он живет и дышит тату, и это чувствуется в каждой его работе. Его татуировки – это настоящие произведения искусства, которые заставляют задуматься и чувствовать.",  # noqa
    "Тату – это свобода для этого мастера. Он создает татуировки, которые отражают индивидуальность и свободу. Его работы – это не просто рисунки на коже, а настоящие произведения искусства.",  # noqa
]


class SalonManager:
    def __init__(self):
        self.salons = Salon.objects.all()

    def create_new_salon(self, name):
        salon = Salon(
            name=name, address="Test address", longitude=0, latitude=0
        )  # noqa
        salon.save()
        self.salons = Salon.objects.all()
        return salon

    def get_random_salon(self):
        return random.choice(self.salons)

    def get_salon_by_name(self, name):
        return self.salons.filter(name=name).first()

    def list_salons(self):
        return self.salons


class MasterGenerator:
    def __init__(self, salon):
        self.salon = salon
        self.names = [
            "Александр",
            "Михаил",
            "Дмитрий",
            "Артем",
            "Иван",
            "Максим",
            "Даниил",
            "Андрей",
            "Кирилл",
            "Никита",
            "Анна",
            "Мария",
            "Елена",
            "Дарья",
            "София",
            "Алиса",
            "Виктория",
            "Полина",
            "Екатерина",
            "Ксения",
        ]
        self.test_images_dir = os.path.join(
            settings.MEDIA_ROOT, "test", "masters"
        )  # noqa
        self.test_images = [
            f
            for f in os.listdir(self.test_images_dir)
            if f.endswith((".jpg", ".jpeg", ".png"))
        ]

    def random_experience(self):
        return random.randint(1, 10)

    def random_rating(self):
        return random.uniform(1.0, 5.0)

    def random_price(self):
        return Decimal(random.randint(1000, 15000))

    def generate_phone(self):
        return f"+7{random.randint(900, 999)}{random.randint(1000000, 9999999)}"  # noqa

    def random_text(self):
        return random.choice(texts)

    def random_name(self):
        return random.choice(self.names)

    def create_master(self):
        if not self.test_images:
            raise ValueError("No test images found in media/test/masters/")

        image_name = random.choice(self.test_images)
        source_path = os.path.join(self.test_images_dir, image_name)

        master = Master(
            salon=self.salon,
            name=self.random_name(),
            phone=self.generate_phone(),
            start_cost=self.random_price(),
            rating=self.random_rating(),
            experience=self.random_experience(),
            short_description=self.random_text(),
        )

        master.save()

        new_image_name = f"master_{master.id}_{image_name}"
        target_path = os.path.join("masters", new_image_name)
        master.image.name = target_path

        os.makedirs(os.path.join(settings.MEDIA_ROOT, "masters"), exist_ok=True)  # noqa

        copy2(source_path, os.path.join(settings.MEDIA_ROOT, target_path))
        master.save()

        return master


class Command(BaseCommand):
    help = "Generate masters for a salon"

    def add_arguments(self, parser):
        parser.add_argument(
            "count", type=int, help="Number of masters to generate"
        )  # noqa
        parser.add_argument(
            "--new-salon", action="store_true", help="Create a new salon"
        )
        parser.add_argument(
            "--salon-name", type=str, help="Name of the new salon"
        )  # noqa

    def handle(self, *args, **options):
        count = options["count"]
        create_new_salon = options["new_salon"]
        salon_name = options["salon_name"]

        salon_manager = SalonManager()

        if create_new_salon:
            if not salon_name:
                self.stdout.write(
                    self.style.ERROR("New salon name is required")
                )  # noqa
                return
            salon = salon_manager.create_new_salon(salon_name)
        else:
            salons = salon_manager.list_salons()
            if not salons:
                self.stdout.write(self.style.ERROR("No salons found"))
                return

            self.stdout.write("Choose a salon:")
            for idx, salon in enumerate(salons):
                self.stdout.write(f"{idx + 1}. {salon.name}")

            choice = input(
                "Enter the number of the salon (or 'random' for a random choice): "  # noqa
            )
            if choice.lower() == "random":
                salon = salon_manager.get_random_salon()
            else:
                try:
                    choice = int(choice)
                    salon = salons[choice - 1]
                except (ValueError, IndexError):
                    self.stdout.write(self.style.ERROR("Invalid choice"))
                    return

        master_generator = MasterGenerator(salon)

        for i in range(count):
            try:
                master = master_generator.create_master()
                self.stdout.write(f"Created master: {master.name}")
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error creating master: {str(e)}")
                )  # noqa

        self.stdout.write(self.style.SUCCESS("Successfully generated masters"))
