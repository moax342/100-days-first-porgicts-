#here we will test if the entered number is odd or even

testedNumber =int(input("Enter th number that you want to be tested if its even or odd\n"))

if testedNumber % 2==1:
    print(f"The number {testedNumber} is odd")
else:
    print(f"THe number {testedNumber} is even")