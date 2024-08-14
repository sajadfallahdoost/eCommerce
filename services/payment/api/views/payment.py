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

# from django.conf import settings
# import requests
# import json


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
        callback_url = request.build_absolute_uri(reverse('callback_gateway'))
        bank.set_client_callback_url(callback_url)
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        context = bank.get_gateway()
        return render(request, "redirect_to_bank.html", context=context)
    except AZBankGatewaysException as e:
        logging.critical(e)
        return render(request, "redirect_to_bank.html")


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


# if settings.SANDBOX:
#     sandbox = 'sandbox'
# else:
#     sandbox = 'www'

# ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

# amount = 1000  # Rial / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# phone = 'YOUR_PHONE_NUMBER'  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://127.0.0.1:8080/verify/'


# def send_request(request):
#     data = {
#         "MerchantID": settings.MERCHANT,
#         "Amount": amount,
#         "Description": description,
#         "Phone": phone,
#         "CallbackURL": CallbackURL,
#     }
#     data = json.dumps(data)
#     # set content length by data
#     headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#     try:
#         response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

#         if response.status_code == 200:
#             response = response.json()
#             if response['Status'] == 100:
#                 return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
#             else:
#                 return {'status': False, 'code': str(response['Status'])}
#         return response

#     except requests.exceptions.Timeout:
#         return {'status': False, 'code': 'timeout'}
#     except requests.exceptions.ConnectionError:
#         return {'status': False, 'code': 'connection error'}


# def verify(authority):
#     data = {
#         "MerchantID": settings.MERCHANT,
#         "Amount": amount,
#         "Authority": authority,
#     }
#     data = json.dumps(data)
#     # set content length by data
#     headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
#     response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

#     if response.status_code == 200:
#         response = response.json()
#         if response['Status'] == 100:
#             return {'status': True, 'RefID': response['RefID']}
#         else:
#             return {'status': False, 'code': str(response['Status'])}
#     return response
