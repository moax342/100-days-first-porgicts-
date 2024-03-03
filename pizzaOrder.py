print("Welcome to our Pizza order delivery \n Small Pizza : $15\n Medium Pizza : $20\n Large Pizza : $25")
print("\nPepperoni for Small pizza : +$2 \n Pepperoni for Medium and Large : +$3")
print("\nExtra Cheese for any size : +$1")
# Order Inputs here.
size = input("What size of Pizza do you want? 'S','M','L'\n")
add_pepperoni = input("Do you want Pepperoni? 'Y' ,'N' \n")
extra_cheese = input("Do you want extra Cheese?'Y' , 'N' \n")
bill = 0
pepperoni_bill = 0
final_bill = 0
# Pizza order code
if size == "S":
    bill = 15
elif size == "M":
    bill = 25
elif size == "L":
    bill = 25
else:
    print("The size you entered is not on the menu")
# pepperoni Code.
if add_pepperoni == "Y" and size == "S":
    pepperoni_bill = 2
elif add_pepperoni == "Y":
    pepperoni_bill = 3
# Extra Cheese Code.
if extra_cheese == "Y":
    final_bill = pepperoni_bill + bill + 1
else:
    final_bill = pepperoni_bill + bill
print(f"Your final Bill is {final_bill}")
