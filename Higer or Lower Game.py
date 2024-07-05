import random as Ran
import os
from art import logo
from art import vs
from game_data import data

# To maintain score of the user
Score = 0

# To loop the game
play_again = True

# To clear the view
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# to create validation
def validation():
    global Score
    global user_input
    global play_again
    global account_a
    global account_b
    if user_input == "a":
        if account_a["Count"] > account_b["Count"]:
            print("It is correct")
            Score += 1
            account_a = account_b
            input("Press Enter to continue...")
            clear_screen()
        elif account_a["Count"] == account_b["Count"]:
            print("its a draw")
        else:
            play_again = False
            print(f"You Loose Buddy, Your score is : {Score} - Dont go cry to your mama !!")
            print(Score)
    if user_input == "b":
        if account_b["Count"] > account_a["Count"]:
            print("It is correct")
            Score += 1
            account_a = account_b
        elif account_b["Count"] == account_a["Count"]:
            print("its a draw")
        else:
            play_again = False
            print(f"You Loose Buddy, Your score is : {Score} - Dont go cry to your mama !!")


while play_again:

    print(logo)
    print("welcome to Higher - Lower Game")

    # This is to show a and b from which user can compare
    random_data_1 = Ran.choice(data)
    random_data_2 = Ran.choice(data)

    # To make sure data 1 and data 2 are not the same
    if random_data_1 == random_data_2:
        random_data_2 = Ran.choice(data)

    # To fetch the user name and other details from the data dict
    account_a_name = random_data_1['name']
    account_a_description = random_data_1['description']
    account_a_country = random_data_1['country']
    account_a_count = random_data_1['follower_count']
    account_b_name = random_data_2['name']
    account_b_description = random_data_2['description']
    account_b_country = random_data_2['country']
    account_b_count = random_data_2['follower_count']

    # Creating an dict
    account_a = {
        'name': account_a_name,
        'description': account_a_description,
        'country': account_a_country,
        'Count': account_a_count,
    }
    account_b = {
        'name': account_b_name,
        'description': account_b_description,
        'country': account_b_country,
        'Count': account_b_count,
    }

    # To print the current score of the user
    print(f"\n Your current score is {Score}\n")

    # To Display account_a and account_b
    print(f"{account_a['name']}, {account_a['description']}, {account_a['country']}")
    print(vs)
    print(f"{account_b['name']}, {account_b['description']}, {account_b['country']}")

    # To let user take a guess
    user_input = input("\n Guess who has more instagram followers ? A or B (Think before you say)\n").lower()
    if user_input not in ["a", "b"]:
        print("Invalid input. Please enter 'a' or 'b'.")
        play_again = False

    # Call Validation
    validation()

else:
    print("Thank you for playing")
