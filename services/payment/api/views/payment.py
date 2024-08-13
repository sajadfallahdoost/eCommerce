import logging
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from azbankgateways import (
    bankfactories,
    models as bank_models,
    default_settings as settings,
)
from services.payment.api.serializers import PaymentRequestSerializer, MetadataSerializer
from services.payment.logic import PaymentLogic
from azbankgateways.exceptions import AZBankGatewaysException
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.urls import reverse
from django.shortcuts import render


@csrf_exempt
def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 50000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = "+989112221234"  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = (
            factory.auto_create()
        )  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url("callback_gateway_view/")
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e


@csrf_exempt
def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse(
        "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت."
    )


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def payment_request(request):
    paymentrequest = PaymentRequestSerializer(data=request.data)

    if paymentrequest.is_valid():
        merchant_id = paymentrequest.validated_data['merchant_id']
        amount = paymentrequest.validated_data['amount']
        description = paymentrequest.validated_data['description']
        callback_url = paymentrequest.validated_data['callback_url']

        # Accessing the metadata, assuming it's passed as part of the main request data
        metadata = paymentrequest.validated_data.get('metadata', {})
        mobile = metadata.get('mobile')
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
