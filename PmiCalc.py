height =input("Enter you height in Meters M:\n")
weight =input("Enter you weight in Kilos K:\n")

f_height=float(height)
f_weight=float(weight)

result=f_weight//(f_height**2)

print(f"your BMI is {result}")