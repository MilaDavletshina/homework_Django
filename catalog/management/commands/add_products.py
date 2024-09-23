from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        prod, _ = Product.objects.get_or_create(name='Беспроводной пылесос', description='Беспроводной пылесос. Наслаждайся уборкой', category='Пылесос', price=11200, created_at='2024-09-23', updated_at='2024-09-23')
        categories = [
            {'name': 'Пылесос','description': 'Tefal Air Force TY6545', 'group': prod}
        ]

        for cat_data in categories:
            category, created = Category.objects.get_or_create(**cat_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added: {category.name} '))
            else:
                self.stdout.write(self.style.SUCCESS(f'already exist: {category.name} '))
