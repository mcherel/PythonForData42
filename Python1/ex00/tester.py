from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

""" height = ["hello", 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26)) """



""" import numpy as np

# random float 0-1
a = np.random.rand(4,2)
print(a)
# random int from -4 to 8
b = np.random.randint(-4,8, size=(3,3))
print(b)

c = np.identity(5)
print(c)

# 11111
# 10001
# 10901
# 10001
# 11111

output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:4,1:4] = z
print(output) """