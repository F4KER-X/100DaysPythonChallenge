from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
user_data = data_manager.get_user_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

# add iata codes to sheet
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# send notification
for destination in sheet_data:
    try:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
    except IndexError:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        notification_manager.send_sms(
            message=message)

# add email to sheet
# first_name = input("What is your first name?\n")
# last_name = input("What is your last name?\n")
# email = input("What is your email?\n")
# email_validation = input("Type your email again\n")
# good_email = False


# if email == email_validation and not data_manager.check_if_email_exists(email=email):
#     print("You're in the club")
#     data_manager.add_user(first_name=first_name,
#                           last_name=last_name, email=email)
# else:
#     print("Email doesn't match/Email already in list")
