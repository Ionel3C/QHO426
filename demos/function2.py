def calc_area:
  l = int(input("What is lenght?"  ))
  w = int(input("What is height?"  ))
  print(f"Area is {l}*{h})



def Rectangle(width, height):
  height = int(input("Enter height"  ))
  w = int(input("Enter width"  ))
  #area
  Area = width * height
  #perimeter
  Perimeter = 2 * (width + height)
  print ("\n Area is: %.2f" %Area)
  print ("\n Perimeter is: %.2f" %Perimeter)

rectangle(width, height)