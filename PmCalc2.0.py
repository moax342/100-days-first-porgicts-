height =float(input("Enter you height in Meters M:\n"))
weight =float(input("Enter you weight in Kilos K:\n"))

result=weight//(height**2)
if result <=18.5:
    print("you are underweight ")
elif result <=25:
    print("Your weight is Normal think god")
elif result <=30:
    print("You are overweight please go and run")
elif result <=35:
    print("you are Obese")
else:
    print(f"go kill your self you are too fat")