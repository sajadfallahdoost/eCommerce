from django.core.management.base import BaseCommand
from account.repository.generator import AccountDataGenerator


class Command(BaseCommand):
    help = 'Generate fake data for the account models'

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            type=int,
            default=100,
            help='Specify the total number of records to generate for each model.'
        )

    def handle(self, *args, **kwargs):
        account_data_generator = AccountDataGenerator()

        try:
            users = account_data_generator.create_users(total=10000)
            self.show_success_msg(f'Created {len(users)} users.')

            corporate_profiles = account_data_generator.create_corporate_profiles(total=50, disable_progress_bar=False)
            self.show_success_msg(f'Created {len(corporate_profiles)} corporate profiles.')

            personal_profiles = account_data_generator.create_personal_profiles(total=50, disable_progress_bar=False)
            self.show_success_msg(f'Created {len(personal_profiles)} personal profiles.')

            addresses = account_data_generator.create_addresses(total=100, disable_progress_bar=False)
            self.show_success_msg(f'Created {len(addresses)} addresses.')

        except Exception as e:
            self.show_error_msg(f'Failed to create data: {str(e)}')

    def show_success_msg(self, msg: str):
        """Displays a success message on the console."""
        self.stdout.write(self.style.SUCCESS(msg))

    def show_error_msg(self, msg: str):
        """Displays an error message on the console."""
        self.stdout.write(self.style.ERROR(msg))
