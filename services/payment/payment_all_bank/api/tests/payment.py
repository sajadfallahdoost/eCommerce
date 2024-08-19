import logging
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from azbankgateways.exceptions import AZBankGatewaysException
from azbankgateways import bankfactories, models as bank_models


class PaymentGatewayTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.amount = 50000
        self.user_mobile_number = "+989112221234"

    @patch('azbankgateways.bankfactories.BankFactory')
    def test_go_to_gateway_view_success(self, mock_factory):
        # Mocking the Bank object and its methods
        mock_bank = mock_factory.return_value.auto_create.return_value
        mock_bank.get_gateway.return_value = {'redirect_url': 'https://bank.url'}

        response = self.client.get(reverse('go_to_gateway'))

        # Assertions
        mock_bank.set_request.assert_called_once()
        mock_bank.set_amount.assert_called_once_with(self.amount)
        mock_bank.set_client_callback_url.assert_called_once()
        mock_bank.set_mobile_number.assert_called_once_with(self.user_mobile_number)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redirect_to_bank.html')
        self.assertContains(response, 'redirect_url')

    @patch('azbankgateways.bankfactories.BankFactory')
    def test_go_to_gateway_view_exception(self, mock_factory):
        # Simulate an exception being raised during bank.ready()
        mock_bank = mock_factory.return_value.auto_create.return_value
        mock_bank.ready.side_effect = AZBankGatewaysException()

        response = self.client.get(reverse('go_to_gateway'))

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redirect_to_bank.html')
        # Check that the error was logged
        with self.assertLogs('root', level='CRITICAL') as cm:
            logging.critical('test log')
            self.assertTrue(any('AZBankGatewaysException' in message for message in cm.output))

    @patch('azbankgateways.bankfactories.BankFactory')
    def test_callback_gateway_view_success(self, mock_factory):
        mock_bank_record = patch('azbankgateways.models.Bank').start()
        mock_bank_record.objects.get.return_value.is_success = True

        response = self.client.get(reverse('callback_gateway'), {'tc': 'test-tracking-code'})

        # Assertions
        mock_bank_record.objects.get.assert_called_once_with(tracking_code='test-tracking-code')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "پرداخت با موفقیت انجام شد.")

    @patch('azbankgateways.bankfactories.BankFactory')
    def test_callback_gateway_view_failure(self, mock_factory):
        mock_bank_record = patch('azbankgateways.models.Bank').start()
        mock_bank_record.objects.get.return_value.is_success = False

        response = self.client.get(reverse('callback_gateway'), {'tc': 'test-tracking-code'})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "پرداخت با شکست مواجه شده است.")

    def test_callback_gateway_view_missing_tracking_code(self):
        response = self.client.get(reverse('callback_gateway'))

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "این لینک معتبر نیست.")

    def test_callback_gateway_view_invalid_tracking_code(self):
        mock_bank_record = patch('azbankgateways.models.Bank').start()
        mock_bank_record.objects.get.side_effect = bank_models.Bank.DoesNotExist

        response = self.client.get(reverse('callback_gateway'), {'tc': 'invalid-code'})

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "این لینک معتبر نیست.")
