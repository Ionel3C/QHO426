#   age(input("What is your curent age?    "))
#   time_left = int(f"90 - age")
#   x == 365
#   z == 12
#   y == 52
# if time == 90:
#   print(f"You have" + (time_left * x), (time_left * y) + "and" + (time_left * y) + left")
  
# run(time)



age = (input("What is your curent age?    "))
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remainig = years_remaining * 365
months_remainig = years_remaining * 12
weeks_remaining = years_remaining * 52
message = f"You have {days_remainig} days, {weeks_remaining} weeks, and {months_remainig} months left."
print(message)