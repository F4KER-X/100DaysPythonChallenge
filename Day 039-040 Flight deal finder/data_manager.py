import requests

SHEETY_PRICES_ENDPOINT = ""
SHEETY_USERS_ENDPOINT = ""


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.users_data = {}
        self.get_user_data()

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.users_data = data['users']
        return self.users_data

    def add_user(self, first_name, last_name, email):
        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }}
        response = requests.put(
            url=f"{SHEETY_USERS_ENDPOINT}/{len(self.users_data) + 2}", json=new_data)

        print(response.text)

    def check_if_email_exists(self, email):
        for user in self.users_data[:len(self.users_data)]:
            if email in user['email']:
                return True
            return False
