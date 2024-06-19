from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Generate all data for warehouse, shop, and account models'

    def handle(self, *args, **kwargs):
        try:
            self.stdout.write(self.style.SUCCESS('Starting data generation for all apps...'))

            call_command('generate_account_data')
            self.stdout.write(self.style.SUCCESS('Account data generated successfully.'))

            call_command('generate_warehouse_data')
            self.stdout.write(self.style.SUCCESS('Warehouse data generated successfully.'))

            call_command('generate_shop_data')
            self.stdout.write(self.style.SUCCESS('Shop data generated successfully.'))

            self.stdout.write(self.style.SUCCESS('All data generated successfully.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to generate data: {str(e)}'))
