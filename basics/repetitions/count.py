n = int(input("How many live cables should I avoid ?"   ))
if n > 3:
  print("Too many cables for remove.")
elif n == 0:
  print("No cable was removed.")
elif n == 3:
  print("Avoiding...Done! 1 live cables avoided.", "\nAvoiding...Done! 2 live cables avoided.", "\nAvoiding...Done! 3 live cables avoided.")
  print("All live cables have been avoided.")
  