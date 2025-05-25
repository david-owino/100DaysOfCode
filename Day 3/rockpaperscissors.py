# script to demonstrate rock paper scissors game between computer and human player

import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_choices = [rock, paper, scissors]
name_choices = ["R", "P", "S"]

print("Welcome to Rock Paper Scissors! Let's see if you can beat the machine 😌")
player_choice = input("What's your pick: R for Rock, P for Paper, S for Scissors?\n").upper()

if player_choice not in name_choices:
    print("Invalid choice. Please enter R, P, or S.")
else:
    computer_index = random.randint(0, 2)
    computer_choice = name_choices[computer_index]

    print("\nYou chose:")
    print(ascii_choices[name_choices.index(player_choice)])

    print("Computer chose:")
    print(ascii_choices[computer_index])

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "R" and computer_choice == "S") or \
         (player_choice == "P" and computer_choice == "R") or \
         (player_choice == "S" and computer_choice == "P"):
        print("Human wins! 🥳")
    else:
        print("Computer wins! 💻💥")
