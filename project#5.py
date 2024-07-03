import os
print("*******Welcom to The SILENT AUCTION Program*******")
def find_winner(bidder_derails):
    highest_bid=0
    winner=""
    for bidder in bidder_derails:
        bidder_price=bidder_derails[bidder]
        if bidder_price>highest_bid:
            highest_bid=bidder_price
            winner=bidder
    print(f"here is the list of all the bidder:{bidder_derails}")
    print(f"the winner is {winner} with a bid price of {highest_bid}")
bidder_date={}
end_of_bidding=False
while not end_of_bidding:
    name=input("what is your name?:")
    price=int(input("what is your bid?:"))
    bidder_date[name]=price
    more_bidders=input("Are there more bidder? Type 'yes' or 'no':").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_date)
    elif more_bidders=='yes':
        os.system('cls')
