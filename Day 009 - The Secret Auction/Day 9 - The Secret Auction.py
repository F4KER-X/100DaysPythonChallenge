from art import logo
import os


def clear():
    return os.system('cls')


print(logo)


bidders = {}

stop = False

while not stop:
    bidder_name = input("What is your name?: ")
    bidder_price = int(input("What's your bid?: $"))

    bidders[bidder_name] = bidder_price

    ask_for_more = input(
        "Are there any other bidders? Type 'yes' or 'no' ").lower()

    if ask_for_more == 'no':
        clear()
        stop = True
    elif ask_for_more == 'yes':
        clear()
    else:
        print("Wrong input. Bid ended")
        break


def max_bidder(bidder_dic):
    max_bid = 0
    for key in bidder_dic:
        value = bidder_dic[key]

        if value > max_bid:
            max_bid = value
            max_name = key
    print(f'The winner is {max_name} with a bid of ${max_bid}')


max_bidder(bidders)
