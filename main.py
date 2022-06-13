#Rock Paper Scissors Game
import random

while True:
    possible_choice = ["R", "P", "S"]
    user_choice = input("Choose One \nR for Rock, \nP for Paper \nS for Scissors\n: ")
    
    while user_choice not in possible_choice:
        user_choice = input("Enter Valid Input: ")
        break


    if user_choice == "R":
        user_choice_name = "Rock"
    elif user_choice == "P":
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissors"

    computer_choice = random.choice(possible_choice)
    if computer_choice == "R":
        computer_choice_name = "Rock"
    elif computer_choice == "P":
        computer_choice_name = "Paper"
    else:
        computer_choice_name = "Scissors"

    print(f"\nPlayer ({user_choice_name}): CPU: ({computer_choice_name}).\n")

    if(user_choice == computer_choice):
        print("Both You and Computer chose the same thing")
        result = "Same"
    
    elif((user_choice == "R" and computer_choice == "P") or 
        (user_choice == "P" and computer_choice == "R")):
        print("Paper Wins =>", end = "")
        result = "Paper"
    
    elif((user_choice == "R" and computer_choice == "S") or
        (user_choice == "S" and computer_choice == "R")):
        print("Rock wins =>", end = "")
        result = "Rock"

    else:
        print("Scissors wins =>", end = "")
        result = "Scissors"
    
    if  result == "Same":
        print("<== Draw ==>")
        continue
    elif result == user_choice_name:
        print("<== You Win ==>")
    else:
        print("<== Computer Wins ==>")
    
    print("Do you want to play again? (Y/N)")
    ans = input()
    
    if ans == "N" or ans == "n":
        break

    print("\nThanks for Playing")