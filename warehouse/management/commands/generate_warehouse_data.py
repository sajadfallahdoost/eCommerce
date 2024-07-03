from django.core.management.base import BaseCommand
from warehouse.repository.generator import WarehouseDataGenerator


class Command(BaseCommand):
    help = 'Generate fake data for the warehouse models'

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            type=int,
            default=300,
            help='Specify the total number of records to generate for each model.'
        )

    def handle(self, *args, **kwargs):
        warehouse_data_generator = WarehouseDataGenerator()

        try:
            brands = warehouse_data_generator.create_brands(total=100)
            self.show_success_msg(f'Created {len(brands)} brands.')

            tags = warehouse_data_generator.create_tags(total=100)
            self.show_success_msg(f'Created {len(tags)} tags.')

            categories = warehouse_data_generator.create_categories(total=100)
            self.show_success_msg(f'Created {len(categories)} categories.')

            attribute_values = warehouse_data_generator.create_attribute_values(total=80)
            self.show_success_msg(f'Created {len(attribute_values)} attribute values.')

            products = warehouse_data_generator.create_products(total=300)
            self.show_success_msg(f'Created {len(products)} products.')

            packs = warehouse_data_generator.create_packs(total=200)
            self.show_success_msg(f'Created {len(packs)} packs.')

        except Exception as e:
            self.show_error_msg(f'Failed to create data: {str(e)}')

    def show_success_msg(self, msg: str):
        """Displays a success message on the console."""
        self.stdout.write(self.style.SUCCESS(msg))

    def show_error_msg(self, msg: str):
        """Displays an error message on the console."""
        self.stdout.write(self.style.ERROR(msg))
