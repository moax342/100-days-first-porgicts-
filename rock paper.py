import random


rock='''ROCK '''
paper='''PAPER '''
siccer='''SIZER '''
game =[rock,paper,siccer]
computerchoise=random.randint(0,3)
choise = int(input("type 0 for rock 1 for paper 2 for siccer"))
print(f"you chose :\n {game[choise]}")
print(f"computer chose :\n {game[computerchoise]}")
if choise==computerchoise:
    print(" you drow")
elif choise>computerchoise:
    print(" you win")
elif choise<computerchoise:
    print(" you lose")



