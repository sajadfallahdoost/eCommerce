from django.core.management.base import BaseCommand
from shop.repository.generator import ShopDataGenerator


class Command(BaseCommand):
    help = 'Generate fake data for the shop models'

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            type=int,
            default=100,
            help='Specify the total number of records to generate for each model.'
        )

    def handle(self, *args, **kwargs):
        total: int = kwargs['total']
        shop_data_generator = ShopDataGenerator()

        try:
            order_addresses = shop_data_generator.create_order_addresses(total=total, disable_progress_bar=False)
            self.show_success_msg(f'Created {len(order_addresses)} order addresses.')

            carts = shop_data_generator.create_carts(total=total, disable_progress_bar=False)
            self.show_success_msg(f'Created {len(carts)} carts.')

            orders = shop_data_generator.create_orders(total=total, disable_progress_bar=False)
            self.show_success_msg(f'Created {len(orders)} orders.')

            cart_items = shop_data_generator.create_cart_items(total=total, disable_progress_bar=False)
            self.show_success_msg(f'Created {len(cart_items)} cart items.')
        except Exception as e:
            self.show_error_msg(f'Failed to create data: {str(e)}')

    def show_success_msg(self, msg: str):
        """Displays a success message on the console."""
        self.stdout.write(self.style.SUCCESS(msg))

    def show_error_msg(self, msg: str):
        """Displays an error message on the console."""
        self.stdout.write(self.style.ERROR(msg))
