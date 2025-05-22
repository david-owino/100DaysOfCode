# This is a simple pizza ordering program that calculates the final bill based on user input.
# It prompts the user for the size of the pizza, whether they want pepperoni and/or extra cheese,
# and then calculates the total cost based on the choices made.
# The program uses conditional statements to determine the cost of the pizza based on the size and toppings.
# The final bill is then printed to the console.
 

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
# Initialize the final bill to 0
final_bill = 0

#calculate bill based pn price
if size == "S":
    final_bill += 15
elif size == "M":
    final_bill += 20
elif size == "L":
    final_bill += 25
else:
    print("Invalid size. Please choose S, M, or L.")

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