total=input("What is the total bill?")
totalAsF=float(total)
PrecnTage=input("What percentage tip you would like to give? 10,12 or 15?")
PrecnAsF=float(PrecnTage)
PrecnTageAsF=PrecnAsF/100 + 1
numOfPpl=input("How many people to split the bill")
numPpl=int(numOfPpl)
amount = round((totalAsF /numPpl )*PrecnTageAsF, 2)
print(f"Each person of the {numPpl} Should pay: {amount}")