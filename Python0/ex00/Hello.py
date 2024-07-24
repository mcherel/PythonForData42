#!/usr/bin/env python3.10

# replace value inside a list
def replace_in_list(list, ix, val):
    list[ix] = val

# replace value inside a tuple by slicing
def replace_in_tuple(tup, ix, val):
    return tup[:ix] + (val,) + tup[ix + 1:]

# replace value inside a set
def replace_in_set(s, new, old):
    s.discard(old)
    s.add(new)

# replace value inside a dict
def replace_in_dict(dict, key, val):
    dict[key] = val

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# replacing value inside a list
replace_in_list(ft_list, 1, 'World!')
print(ft_list)

# replacing value isnide a tuple 
ft_tuple = replace_in_tuple(ft_tuple, 1, "France!")
# print(id(ft_tuple))
print(ft_tuple)
# print(id(ft_tuple))

# replacing value isnide a set
# print(id(ft_set))
replace_in_set(ft_set, "Paris!", "tutu!")
# print(id(ft_set))
print(ft_set)

# replacing value isnide a dictionnary
replace_in_dict(ft_dict, "Hello", "42Paris!")
print(ft_dict)

