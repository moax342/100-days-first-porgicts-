def prime_checker(number):
    if number %2== 0 or number %3==0:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")

num =int(input("Enter a number to be checked"))
prime_checker(num)