# step1
import random
word_list=["ardvark" , "baboon" , "camel"]

# choosing the word:
chosen_word=random.choice(word_list)
display=[]
lives=6
for l in range(len(chosen_word)):
    display+="_"
print(display)
# -----------------------------------------------------------
while "_" in display and lives >0:
    # entering the letter
    chosen_letter=input("Guess A Letter:\n").lower()
    # looping throughout the letters
    for position in range(0,len(chosen_word)):
        letter =chosen_word[position]
        if letter == chosen_letter:
            display[position]=letter
    lives -= 1
    print(display)
# ------------------------------------------------------------
if "_" not in display:
    print("You Win")
else:
    print("You lose")