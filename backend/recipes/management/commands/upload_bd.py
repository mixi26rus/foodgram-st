import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from recipes.models import Ingredient


class Command(BaseCommand):
    help = "Импорт ингредиентов из JSON-файла в базу данных"

    def handle(self, *args, **kwargs):
        json_path = Path(settings.BASE_DIR) / "data" / "ingredients.json"

        if not json_path.is_file():
            self.stdout.write(
                self.style.ERROR(f"Не удалось найти файл: {json_path}")
            )
            return

        try:
            with open(json_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                new_ingredients = [Ingredient(**entry) for entry in data]

                existing_count = Ingredient.objects.count()
                Ingredient.objects.bulk_create(
                    new_ingredients, ignore_conflicts=True)
                added_count = Ingredient.objects.count() - existing_count

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Добавлено ингредиентов: {added_count}")
                )
        except json.JSONDecodeError:
            self.stdout.write(
                self.style.ERROR("Ошибка: файл содержит некорректный JSON")
            )
        except Exception as error:
            self.stdout.write(
                self.style.ERROR(f"Произошла ошибка: {str(error)}")
            )
