from django import forms


class PaymentForm(forms.Form):
    amount = forms.IntegerField(label="Amount", required=True)
    cell_number = forms.CharField(label="Mobile Number", required=True)
    redirect_url = forms.URLField(label="Redirect URL", required=True)
    res_num = forms.CharField(label="Transaction Number", required=True)
