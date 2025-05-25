# script to pick a random name out of a list
# it simulates a random person to be picked to pay a bill

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#option 1
random_index = random.randint(0, len(friends) -1)
paying_friend = friends[random_index]
print(paying_friend)

#option 2
print(random.choice(friends))

