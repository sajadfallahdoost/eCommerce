import logging
import requests
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from azbankgateways import (
    bankfactories,
    models as bank_models,
    default_settings as settings,
)
from azbankgateways.exceptions import AZBankGatewaysException


@csrf_exempt
def go_to_gateway_view(request):
    if request.method == 'POST':
        # Get the CSRF token
        csrf_token = get_token(request)

        # Reading the amount and other details
        amount = 10000000
        user_mobile_number = "+989112221234"  # Optional

        factory = bankfactories.BankFactory()
        try:
            bank = factory.create()
            bank.set_request(request)
            bank.set_amount(amount)
            bank.set_client_callback_url("callback-gateway")
            bank.set_mobile_number(user_mobile_number)  # Optional

            bank_record = bank.ready()

            # URL for redirecting to the payment gateway
            redirect_url = bank.redirect_gateway_url("test/")

            # Add custom headers
            headers = {
                'X-SANDBOX': '1',
                'X-CSRFToken': csrf_token,
                'Content-Type': 'application/json',
            }

            # Make a request to the payment gateway
            response = requests.post(redirect_url, headers=headers)

            # Handle the response from the payment gateway
            if response.status_code == 200:
                return JsonResponse({'redirect_url': response.url})
            else:
                logging.error(f"Failed to redirect to the payment gateway: {response.text}")
                return HttpResponse("An error occurred while processing the payment.", status=500)

        except AZBankGatewaysException as e:
            logging.critical(e)
            return HttpResponse("An error occurred: {}".format(e), status=500)

    return HttpResponse("Invalid request method", status=405)


@csrf_exempt
def payment_request(request):
    if request.method == 'POST':
        csrf_token = get_token(request)
        
        url = "https://api.zarinpal.com/pg/v4/payment/request.json"
        merchant_id = "1344b5d4-0048-11e8-94db-005056a205be"  # replace with your actual merchant ID
        amount = 10000  # amount in Rials
        description = "افزایش اعتبار کاربر شماره ۱۱۳۴۶۲۹"
        callback_url = "http://yourdomain.com/payment/verify/"  # replace with your actual callback URL
        headers = {
            'X-CSRFToken': csrf_token,
            'Content-Type': 'application/json',
        }

        payload = {
            "merchant_id": merchant_id,
            "amount": amount,
            "description": description,
            "callback_url": callback_url,
            "metadata": {"mobile": "09121234567", "email": "info.test@gmail.com"}
        }

        response = requests.post(url, headers=headers, json=payload)

        # Check response status and content before attempting to parse JSON
        try:
            response_data = response.json()
        except ValueError as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Failed to parse JSON response',
                'response_status_code': response.status_code,
                'response_content': response.text,
            }, status=500)

        if response_data['data']['code'] == 100:
            authority = response_data['data']['authority']
            payment_url = f"https://www.zarinpal.com/pg/StartPay/{authority}"
            return JsonResponse({'url': payment_url})
        else:
            return JsonResponse(response_data['errors'], status=400)
    else:
        return HttpResponse("Invalid request method", status=405)
