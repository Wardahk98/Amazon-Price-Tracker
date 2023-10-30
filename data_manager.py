import requests
from keys import sheety_header, sheety_post_url


class Datamanager:
    def __init__(self):
        self.sheety_post_url = sheety_post_url
        self.sheety_header = sheety_header
        self.response = requests.get(url=self.sheety_post_url, headers=self.sheety_header)
        self.response.raise_for_status()
        self.data = self.response.json()

    def add_data(self, p_name, a_url, p_price, r_price, u_email):
        body = {
            "sheet1": {
                "productName": p_name,
                "amazonLink": a_url,
                "productPrice": p_price,
                "reducedPrice": r_price,
                "userEmail": u_email,
            }
        }
        put = requests.post(url=self.sheety_post_url, headers=self.sheety_header, json=body)
        put.raise_for_status()
