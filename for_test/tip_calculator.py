print("Welcome to the tip calculator !")
total_bill = float(input("What was the total bill?   £"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?  "))
person = int(input("How many people to split the bill?  "))
bill = (percentage_tip / 100 * total_bill) + total_bill
amount_per_person = bill / person
round(amount_per_person, 2)
print(f"Each person should pay: £{amount_per_person}")