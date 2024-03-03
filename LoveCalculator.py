print("Welcome to the Love calculator ")
name1=input("Enter your name \n").lower()
name2=input("Enter your loved one name \n").lower()

concat_name=name1+name2
amountOfT=concat_name.count("t")
amountOfR=concat_name.count("r")
amountOfU=concat_name.count("u")
amountOfE=concat_name.count("e")
trueNumber =amountOfT+amountOfR+amountOfU+amountOfE

amountOfL=concat_name.count("l")
amountOfO=concat_name.count("o")
amountOfV=concat_name.count("v")
LoveNumber=amountOfL+amountOfO+amountOfV+amountOfE

loveScore =str(trueNumber)+str(LoveNumber)

print(f" Your Score is {loveScore}")
