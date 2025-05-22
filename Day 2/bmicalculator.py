# script to calculate bmi with interpretation of results

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    interpretation = "Underweight"
elif 18.5 <= bmi < 24.9:
    interpretation = "Normal weight"
elif 25 <= bmi < 29.9:
    interpretation = "Overweight"
else:
    interpretation = "Obesity"
print(f"Your BMI is: {bmi:.2f}")
print(f"Interpretation: {interpretation}")

