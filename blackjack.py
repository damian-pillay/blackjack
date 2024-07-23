from os import system
from random import choice
import time

deck = {str(i): i for i in range(2, 11)}
deck.update({"J": 10, "Q": 10, "K": 10, "A": 11})

deck_list = list(deck.items())

def main():
    while True:
        system("cls")
        ask = input("Do you want to play blackjack? (Type 'yes' or 'no')\n>>> ").strip().lower()

        if ask == 'yes':
            system('cls')
            game = blackjack()
        elif ask == 'no':
            break
        else:
            print("Please enter 'yes' or 'no' only.")
            time.sleep(5)
            continue
    
        if game == 1 :
            time.sleep(1.5)
            print("\nYou win!\n")
            time.sleep(2)
        elif game == 0:
            time.sleep(1.5)
            print("\nYou Lose!\n")
            time.sleep(2)
        else:
            time.sleep(1.5)
            print("\nDraw!\n")
            time.sleep(2)

def blackjack():
    my_hand = [random_card(), random_card()]
    cpu_hand = [random_card(), random_card()]

    while True:
        if my_hand[1][0] == 'A' and my_hand[0][0] == 'A':
            my_hand[1] == random_card()
        else:
            break

    my_hand_list = []
    ace_count = 0
    deduction = 0

    my_score = my_hand[0][1] + my_hand[1][1]
    
    for i in range(len(my_hand)):
        if (my_hand[i][0] == 'A'):
            ace_count += 1

    for card in my_hand:
        my_hand_list.append(card[0])
    
    my_score = my_hand[0][1] + my_hand[1][1]
    opp_score = cpu_hand[0][1] + cpu_hand[1][1]

    print(f"\nYour Hand: {my_hand_list}\nYour Score: {my_score}\n")
    print(f"Opponents first card: {cpu_hand[0][0]}\nOpponent Score: {cpu_hand[0][1]}\n")

    while True:
        ask = input("Would You like another card? (Type 'yes' or 'no')\n>>> ").strip().lower()

        if ask == 'yes':
            system('cls')
            new_card = random_card()

            if new_card[0] == 'A':
                ace_count += 1

            my_hand_list.append(new_card[0])
            my_score += new_card[1]

            for i in range(len(my_hand_list)):
                if (my_hand_list[i] == 'A') and (my_score > 21) and (deduction < ace_count):
                    # my_hand[i][1] = 1
                    my_score -= 10
                    deduction += 1

            print(f"\nYour Hand: {my_hand_list}\nYour Score: {my_score}\n")

            if my_score > 21:
                print(f"Your Opponent's Hand: ['{cpu_hand[0][0]}', '{cpu_hand[1][0]}']\nOpponent Score: {opp_score}\n")
                print("Bust!")
                return 0
            else:
                print(f"Opponents first card: {cpu_hand[0][0]}\nOpponent Score: {cpu_hand[0][1]}\n")
                continue
        elif ask == 'no':
            system('cls')
            print("\nFinal Results:")
            print(f"\nYour Hand: {my_hand_list}\nYour Score: {my_score}\n")
            print(f"Your Opponent's Hand: ['{cpu_hand[0][0]}', '{cpu_hand[1][0]}']\nOpponent Score: {opp_score}\n")
            if opp_score < my_score:
                return 1
            elif my_score < opp_score <= 21:
                return 0
            elif opp_score > 21:
                print("Your Opponent Bust!")
                return 1
            elif my_score == opp_score:
                return 2
        else:
            print("Please enter 'yes' or 'no' only.")
            continue


def random_card():
    """Gives a tuple with of a random card - first element is the card name, second is the value"""
    return choice(deck_list)

main()