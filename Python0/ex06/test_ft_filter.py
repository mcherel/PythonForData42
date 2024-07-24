import ft_filter as f

print("_________________________")
print(filter.__doc__)
print("_________________________")
print(f.ft_filter.__doc__)

print("_________________________")
print("TEST 0")
print("_________________________")

ages = [0, 5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

print("_________________________")
for x in filter(None, ages):
  print(x)
print("_________________________")
for x in f.ft_filter(None, ages):
  print(x)

print("_________________________")
print("TEST 1")
print("_________________________")

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
print("_________________________")

print("_________________________")
print("TEST 2")
print("_________________________")

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)  # filter object
even_numbers2 = f.ft_filter(is_even, numbers)  # filter object

# Convert filter object to a list to see the result
even_numbers_list = list(even_numbers)
even_numbers_list2 = list(even_numbers2)
print(even_numbers_list)  # Output: [2, 4, 6]
print(even_numbers_list2)  # Output: [2, 4, 6]

print("TEST 3")
print("_________________________")

numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(None,numbers)))
print(list(f.ft_filter(None,numbers)) )
print("_________________________")

print("ERROR MANAGEMENT")
#a = filter()
#print(a)
a2 = f.ft_filter()
print(list(a2))
print(a2)
print("_________________________")

#a = filter(True,ages)
#print(a)
#for i in a:
#  print(a)
a2 = f.ft_filter(True,ages)
#a = filter(2, 1, 3)
a2 = f.ft_filter(2, 1, 3)
#a = filter(2, 1)
a2 = f.ft_filter(2, 1)
#a = filter(2, [1])
#for i in a:
#   print(i)
a2 = f.ft_filter(2, [1])
