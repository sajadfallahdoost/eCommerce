from django.shortcuts import render
from services.payment.payment_sep.models import Payment
from services.payment.payment_sep.forms import PaymentForm
from services.payment.payment_sep.logic import SepPaymentService


def initiate_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = Payment.objects.create(
                terminal_id="Your_Terminal_ID",
                amount=form.cleaned_data['amount'],
                res_num=form.cleaned_data['res_num']
            )
            sep_service = SepPaymentService(terminal_id=payment.terminal_id)
            response = sep_service.get_token(
                amount=payment.amount,
                res_num=payment.res_num,
                redirect_url=form.cleaned_data['redirect_url'],
                cell_number=form.cleaned_data['cell_number'],
            )
            if response['status'] == 1:
                payment.ref_num = response['token']
                payment.status = 'token_received'
                payment.save()
                return render(request, 'payment_sep/payment_form.html', {'token': payment.ref_num})
            else:
                payment.status = 'error'
                payment.save()
                # PaymentLog.objects.create(payment=payment, message=response['errorDesc'])
                return render(request, 'payment_sep/error.html', {'error': response['errorDesc']})
    else:
        form = PaymentForm()
    return render(request, 'payment_sep/initiate_payment.html', {'form': form})


def verify_payment(request):
    ref_num = request.GET.get('RefNum')
    terminal_number = "Your_Terminal_ID"
    sep_service = SepPaymentService(terminal_id=terminal_number)
    verification = sep_service.verify_transaction(ref_num, terminal_number)
    if verification['Success']:
        return render(request, 'payment_sep/success.html', {'details': verification['TransactionDetail']})
    else:
        return render(request, 'payment_sep/error.html', {'error': verification['ResultDescription']})