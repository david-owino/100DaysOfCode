# script to randomly choose between 'Heads' or 'Tails'

import random

print("Program to pick 'Heads' or 'Tails' at random")
random_value = random.randint(1, 2)

if random_value == 1:
    print("Heads")
else:
    print("Tails")