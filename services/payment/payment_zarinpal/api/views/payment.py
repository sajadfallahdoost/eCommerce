from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from services.payment.payment_zarinpal.api.serializers import PaymentRequestSerializer
from services.payment.payment_zarinpal.logic import PaymentLogic

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def payment_zarinpal(request):
    paymentrequest = PaymentRequestSerializer(data=request.data)
    # breakpoint()

    if paymentrequest.is_valid():
        # breakpoint()
        merchant_id = paymentrequest.validated_data['merchant_id']
        amount = paymentrequest.validated_data['amount']
        description = paymentrequest.validated_data['description']
        callback_url = paymentrequest.validated_data['callback_url']

        # Accessing the metadata, assuming it's passed as part of the main request data
        metadata = paymentrequest.validated_data.get('metadata', {})
        mobile = metadata.get('mobile')
        # breakpoint()
        # breakpoint()

        Payment_Logic = PaymentLogic()
        try:
            # breakpoint()
            payment_data = Payment_Logic.send_information(merchant_id, amount, description, callback_url, mobile)
            # breakpoint()
            authority = payment_data['authority']
            return Response({'message': 'Payment initiated successfully', 'authority': authority}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(paymentrequest.errors, status=status.HTTP_400_BAD_REQUEST)
