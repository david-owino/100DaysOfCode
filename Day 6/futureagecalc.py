# script to calculate the number of weeks left in life based on age
# assuming an average lifespan of 90 years (4680 weeks)

def life_in_weeks(age):
    age_in_weeks = 52 * age
    future_age = 4680 - age_in_weeks
    return future_age  

age = 25  
weeks_left = life_in_weeks(age) 

print(f"You have {weeks_left} weeks left.")  
