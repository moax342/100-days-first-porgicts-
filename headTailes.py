import random
testSeed=int(input("Enter your test the seed Or number"))

random.seed(testSeed)
checkNumber =random.randint(1,2)
if checkNumber==1:
    print("Head")
else:
    print("Tails")
