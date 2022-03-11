i = int(input("How many cables should I remove ?   "))

if i == 0:
  print("Cable not was removed.")
elif i == 1:
     print("Removed cable.")
elif i == 2:
  print("Removed cable.", "\nRemoved cable.")
elif i == 3:
  print("Removed cable.", "\nRemoved cable.", "\nRemoved cable.")
else:
  print("Too many cable was removed.")