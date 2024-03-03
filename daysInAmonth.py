def LeapYear(year):
    """Takes a Year form the user and check if its a leap year or not"""
    if year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
        # Leap Year statement
        return True
    else:
        # Not a Leap Year statement
        return False


months_days = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 31, 30]


def days_in_month(year, month):
    """Return the number of days in year based on its a leap  year or not"""
    if LeapYear(year) and month == 2:
        return 29
    else:
        return months_days[month-1]


year = int(input("Enter the Year that you want to check please \n"))
month = int(input("Enter the month that you want to check\n"))
days = days_in_month(year, month)

print(days)
