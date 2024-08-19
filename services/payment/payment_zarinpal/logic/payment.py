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

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

        try:
            response_data = response.json()
        except ValueError as e:
            raise Exception("Failed to parse JSON response: " + str(e))

        if 'data' not in response_data or 'authority' not in response_data['data']:
            raise Exception("Unexpected response structure")

        return response_data['data']
