import requests


class SepPaymentService:
    BASE_URL = "https://sep.shaparak.ir"

    def __init__(self, terminal_id, action="token"):
        self.terminal_id = terminal_id
        self.action = action

    def get_token(self, amount, res_num, redirect_url, cell_number):
        data = {
            "action": self.action,
            "TerminalId": self.terminal_id,
            "Amount": amount,
            "ResNum": res_num,
            "RedirectUrl": redirect_url,
            "CellNumber": cell_number,
        }
        response = requests.post(f"{self.BASE_URL}/onlinepg/onlinepg", json=data)
        return response.json()

    def verify_transaction(self, ref_num, terminal_number):
        data = {
            "RefNum": ref_num,
            "TerminalNumber": terminal_number,
        }
        response = requests.post(f"{self.BASE_URL}/verifyTxnRandomSessionkey/ipg/VerifyTransaction", json=data)
        return response.json()

    def reverse_transaction(self, ref_num, terminal_number):
        data = {
            "RefNum": ref_num,
            "TerminalNumber": terminal_number,
        }
        response = requests.post(f"{self.BASE_URL}/verifyTxnRandomSessionkey/ipg/ReverseTransaction", json=data)
        return response.json()
