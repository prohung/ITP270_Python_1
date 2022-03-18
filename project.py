#Compare and find the oldest out of the 3
age_of_x = 7
age_of_y = 9
age_of_z = 11

if age_of_x > age_of_y:
  if age_of_x > age_of_z:
    print("x is the oldest")
  else:
    print("z is the oldest")
else:
  if age_of_y > age_of_z:
    print("y is the oldest")
  else:
    print("z is the oldest")


#Another way of if nesting
if age_of_x > age_of_y and age_of_x > age_of_z:
  print("x is the oldest")
elif age_of_y > age_of_x and age_of_y > age_of_z:
  print("y is the oldest")
else:
  print("z is the oldest")