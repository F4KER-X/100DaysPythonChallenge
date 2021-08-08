import datetime
import pandas
import smtplib
import random

# check if file exists and transfer data to dict

try:
    data = pandas.read_csv(r"birthdays.csv")
except FileNotFoundError:
    print("File not found")
else:
    birthday_list = data.to_dict(orient="records")

# get today's day/month
now = datetime.datetime.now()
day = now.day
month = now.month

email = "test@gmail.com"  #Your Email
password = ""  #Password


letter_list = [r"letter_templates\letter_1.txt",
               r"letter_templates\letter_2.txt",
               r"letter_templates\letter_3.txt"]


def choose_letter(name):

    letter = random.choice(letter_list)
    try:
        with open(letter) as letter:
            message = letter.read()
            new_message = message.replace("[NAME]", name)
            return new_message
    except FileNotFoundError:
        print("Letter not found")


def send_email(name, email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(to_addrs=email, from_addr=email,
                            msg=f"Subject: \
                                Happy Birthday\n\n{choose_letter(name)}")


for n in birthday_list:
    birthday_day = n['day']
    birthday_month = n['month']
    birthday_email = n['email']
    birthday_name = n['name']

    if day == birthday_day and month == birthday_month:
        # send email
        send_email(birthday_name, birthday_email)
