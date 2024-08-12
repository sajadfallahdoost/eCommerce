import requests


class PaymentLogic:
    def __init__(self, user=None, phone_number=None):
        self.user = user
        self.phone_number = phone_number

    def send_information(self, merchant_id, amount, description, callback_url, mobile):
        url = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
        headers = {
            'ACCEPT': 'application/json',
            'Content-Type': 'application/json'
        }
        payload = {
            "merchant_id": merchant_id,
            "amount": amount,
            "description": description,
            "callback_url": callback_url,
            "metadata": {
                "mobile": mobile,
            }
        }
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        breakpoint()

        # if response_data['data']['code'] != 100:
        #     raise Exception("Failed to initiate payment: " + response_data['errors'][0]['message'])

        if response.status_code != 200:
            raise Exception(f"Failed with status code: {response.status_code}")

        try:
            response_data = response.json()
        except ValueError as e:
            raise Exception("Failed to parse JSON response: " + str(e))

        return response_data['data']
