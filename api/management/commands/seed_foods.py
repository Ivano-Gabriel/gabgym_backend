# api/management/commands/seed_foods.py

import json
from django.core.management.base import BaseCommand
from api.models import FoodCategory, FoodItem

class Command(BaseCommand):
    help = 'Semeia o banco de dados com as comidas do arquivo foods.json'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando o processo de semeadura de comidas...'))

        # Limpa os dados antigos para evitar duplicatas
        FoodCategory.objects.all().delete()
        FoodItem.objects.all().delete()
        self.stdout.write(self.style.WARNING('Dados de comidas antigos foram limpos.'))

        # Caminho para o nosso arquivo JSON
        json_file_path = 'foods.json'

        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for category_name, items in data.items():
                # Cria a categoria ou pega se já existir
                category, created = FoodCategory.objects.get_or_create(name=category_name)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Categoria "{category_name}" criada.'))

                # Itera sobre os itens de comida da categoria
                for item_data in items:
                    FoodItem.objects.create(
                        category=category,
                        name=item_data['name'],
                        unit=item_data.get('unit', ''),
                        serving_desc=item_data.get('serving_desc', ''),
                        calories=item_data.get('calories', 0),
                        protein=item_data.get('protein', 0),
                        carbs=item_data.get('carbs', 0),
                        fat=item_data.get('fat', 0),
                        image_path=item_data.get('image_path', '')
                    )
                self.stdout.write(self.style.SUCCESS(f'>>> {len(items)} itens de comida adicionados à categoria "{category_name}".'))

        self.stdout.write(self.style.SUCCESS('Semeadura de comidas concluída com sucesso!'))