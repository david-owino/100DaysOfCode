print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
final_bill = 0

#calculate bill based pn price
if size == "S":
    final_bill += 15
elif size == "M":
    final_bill += 20
elif size == "L":
    final_bill += 25

#calculate bill based on extra pepperoni
if pepperoni == "Y":
    if size == "S":
        final_bill += 2
    else:
        final_bill += 3
#calculate bill based on extra cheese
if extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}.") 