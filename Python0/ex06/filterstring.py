import ft_filter as f

print("_________________________")
print(filter.__doc__)
print("_________________________")
print(f.ft_filter.__doc__)

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
adults2 = f.ft_filter(myFunc, ages)

print("_________________________")
for x in adults:
  print(x)
print("_________________________")
for x in adults2:
  print(x)
#a = filter()
#a2 = f.ft_filter()

""" a = filter(True,ages)
for i in a:
  print(a) """
a2 = f.ft_filter(2, 1, 3)