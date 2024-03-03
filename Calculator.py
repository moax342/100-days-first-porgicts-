print("Welcome the Moax's Calculator")


# Adding
def add(n1, n2):
    return n1 + n2


# subtracting
def subtracting(n1, n2):
    return n1 - n2


# multiplying
def multiplying(n1, n2):
    return n1 * n2


# division
def division(n1, n2):
    return n1 / n2


def calculator(n1, n2, sign):
    if sign == "+":
        return add(n1, n2)
    elif sign == "-":
        return subtracting(n1, n2)
    elif sign == "*":
        return multiplying(n1, n2)
    elif sign == "/":
        return division(n1, n2)
    else:
        return "Not a valid Operation"


contin = "yes"
while contin == "yes":
    first_number = float(input("Enter the first Number \n"))
    dev = input("Enter the sign \n + \n -\n *\n /\n")
    second_number = float(input("Enter the second number\n"))
    calc=calculator(first_number, second_number, dev)
    print(f"{first_number}{dev}{second_number} ={calc}")
    cont=input("Do you want to continue 'Yes' or 'No'\n").lower()
    contin=cont