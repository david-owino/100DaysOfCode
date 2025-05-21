# Band name generator. Script takes 2 names and concatenates them together to create a Band name.
# The first name is the name of the city you grew up in.
# The second name is the name of a pet.
# The script will then print out the band name.

city_name = input("What is the name of the city you grew up in?\n")
pet_name = input("What is the name of your pet?\n")
band_name = city_name + " " + pet_name
print("Your band name could be " + band_name)
