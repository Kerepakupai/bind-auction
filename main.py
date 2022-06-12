from art import logo
import os



def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')


def main():
    bidders = {}
    bidding_finished = False

    while not bidding_finished:
        print(logo)
        name = input('What is your name?: ')
        bid_price = int(input('What is your bid?: $'))
        bidders[name] = bid_price
        should_continue = input('Are the any other bidders? Type \'yes\' or \'no\'.\n')
        os.system('clear')

        if should_continue == 'no':
            bidding_finished = True
            find_highest_bidder(bidders)



if __name__ == '__main__':
    main()
