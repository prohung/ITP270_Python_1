#Question #1
#Create a function called middle_element that has 1 lst parameter
def middle_element(lst):
  if len(lst) % 2 != 0:
    middle = float(len(lst))/2 - 0.5
    return lst[int(middle)]
  else:
    middle1 = int((len(lst))/2)
    middle2 = int((len(lst))/2 - 1)
    avg = (lst[middle1] + lst[middle2])/2
    return avg

print(middle_element([5, 2, -10, -4, 4, 5]))

#Question #2