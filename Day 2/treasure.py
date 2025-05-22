# guessing game to find treasure
# This is a simple text-based adventure game where the player has to make choices
# to find a treasure. The player is presented with a series of choices, and based on
# their decisions, they can either win the game or face different game over scenarios.
# The game starts with a welcome message and asks the player if they are ready to start.
# Depending on the player's input, they are guided through a series of choices:
# 1. Choose a direction (left or right).
# 2. Choose to swim or wait.
# 3. Choose a door color (red, blue, or yellow).
# The game ends with different outcomes based on the player's choices, including winning the treasure or facing various game over scenarios.


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
start_game = input("Are you ready to start your Journey?").upper()

if start_game == "Y":
    direction = input("Which way will you go, left or right?").upper()
    if direction == "LEFT":
        action = input("Will you swim or wait?").upper()
        if action == "WAIT":
            door = input("What color door are you picking, Red, Blue or Yellow?").upper()
            if door == "YELLOW":
                print("You found the treasure, YOU WIN!!")
            elif door == "RED":
                print("You were burnt by fire, GAME OVER!!")
            elif door == "BLUE":
                print("You were eaten by BEASTS, GAME OVER!!!")
        else:
            print("You were attacked by a trout, GAME OVER!!")
    else:
        print("You fell into a hole, GAME OVER!!")

else:
    print("Come back when you are more courageous!!")

