birth_year = input("What is your Birth Year?: ")
age = 2022 - int(birth_year)

weight_lbs = input("What is your weight in pounds?: ")
weight_kg = 0.45 * float(weight_lbs)
print("You are " + str(age) + " Yrs old " + "and weigh " + str(weight_kg) + " in kg")
