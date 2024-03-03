import random
seedTest=int(input("Enter your seed value here\n"))
random.seed(seedTest)
namesAsCSV =input("Enter the names with ', ' separated \n")
names=namesAsCSV.split(", ")

theChosenOne=random.randint(0, len(names)-1)
print(f"{names[theChosenOne]} would pay The bill today better luck next time.:)")
