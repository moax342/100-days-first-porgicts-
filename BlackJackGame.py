import random

print("Welcome to Moax's Black Jack Game\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def play_game():
    """all the code related to the gae is in this function"""
    user_cards = []
    computer_cards = []
    is_game_over=False

    def deal_card():
        """deals a card for the computer and the user when its called"""
        return random.choice(cards)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(crads):
        """take a list of cards and return the sum of them"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)

        return sum(crads)
    def compare(user_score,computer_score):
        """takes the user score and computer score and output the winner"""
        if user_score == computer_cards:
            return "It's a draw\n"
        elif computer_score==0:
            return"Computer wins\n"
        elif user_score==0:
            return "You win the game\n"
        elif user_score > 21:
            return "Computer wins\n"
        elif computer_score>21:
            return "You Win\n"
        elif user_score>computer_score:
            return "You win\n"
        else:
            return "Computer wins\n"

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f" your Cards:{user_cards} your score:{user_score}\n")
        print(f" Computer first Card is:{computer_cards[0]} \n")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over =True
        else:
            new_card=input("Do you want to draw another card 'Y' or 'N'\n").lower()
            if new_card=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f" your final hand :{user_cards} your score:{user_score}\n")
    print(f" Computer final hand :{computer_cards} your score:{computer_score}\n")
    print(compare(user_score,computer_score))


while input("Do you want to play game of Black Jack 'Y' or 'N' ")=="y":
    """running the game over and over """
    play_game()


