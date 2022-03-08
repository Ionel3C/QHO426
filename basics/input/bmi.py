def bmi():
  height = int(input("Input your height in meters: "))
  weight = int(input("Input your weight in kilogram: "))
  result = (weight + height)
  print("Your body mass index is: ", round(weight / (height * height), 2))
  return result