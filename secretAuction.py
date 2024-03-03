print("Welcome to the secret auction")

auction_bidders = {}


def who_is_in(name, bid):
    auction_bidders[name] = bid


still_other_bidders = "yes"

while still_other_bidders == "yes":
    name = input("Enter your name?")
    bid = float(input("How much do you want to bid $"))
    who_is_in(name=name, bid=bid)
    still_one=input("Is there any one else wants to bid? 'Yes' Or 'No' ").lower()
    still_other_bidders=still_one

start_amount=0
name=""
for key in auction_bidders:
    if auction_bidders[key]>start_amount:
        start_amount=auction_bidders[key]
        name=key
print(f"{name} Won with a bid of ${start_amount}")