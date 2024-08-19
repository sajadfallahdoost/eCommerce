
import requests
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from services.payment.payment_idpay.api.serializers import Payment_Idpay_Serializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def payment_idpay(request):
    paymentrequest = Payment_Idpay_Serializer(data=request.data)
    # breakpoint()

    if paymentrequest.is_valid():
        # breakpoint()
        order_id = paymentrequest.validated_data["order_id"]
        amount = paymentrequest.validated_data["amount"]
        name = paymentrequest.validated_data["name"]
        mail = paymentrequest.validated_data["mail"]

        # Accessing the metadata, assuming it's passed as part of the main request data
        desc = paymentrequest.validated_data["desc"]
        callback = paymentrequest.validated_data["callback"]
        # breakpoint()
        # breakpoint()
        url = "https://api.idpay.ir/v1.1/payment"
        headers = {
            'ACCEPT': 'application/json',
            'X-API-KEY': '6a7f99eb-7c20-4412-a972-6dfb7cd253a4',
            'Content-Type': 'application/json',
            'X-SANDBOX': "1"
        }
        payload = {
            "order_id": order_id,
            "amount": amount,
            "desc": desc,
            "callback": callback,
            "name": name,
            "mail": mail
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            # breakpoint()
            data = {
                "key": "value"
            }
            return Response(data)
            # response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            return Response({'error': f"HTTP error occurred: {http_err}"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error': f"An error occurred: {err}"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(paymentrequest.errors, status=status.HTTP_400_BAD_REQUEST)
