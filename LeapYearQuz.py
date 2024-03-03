year =int(input("Enter the Year that you want to check please \n"))

if year %4 == 0 and year % 100 != 1 and year % 400 == 0:
    print(f"{year} is a Leap Year Harry")
else:
    print(F"{year} Not a Leap Year try again")