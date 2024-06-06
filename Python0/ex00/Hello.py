#!/usr/bin/env python3.10

#replace value inside a list
def replace_in_list(list, ix, val):
    list[ix] = val

#replace value inside a tuple by slicing
def replace_in_tuple(tup, ix, val):
    return tup[:ix] + (val,) + tup[ix + 1:]

#replace value inside a set
def replace_in_set(s, new, old):
    s.discard(old)
    s.add(new)

#replace value inside a dict
def replace_in_dict(dict, key, val):
    dict[key] = val

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
# replacing value inside a list
replace_in_list(ft_list, 1, 'World!')
#replacing value isnide a tuple 
ft_tuple = replace_in_tuple(ft_tuple, 1, "France!")
replace_in_set(ft_set, "Paris!", "tutu!")
replace_in_dict(ft_dict, "Hello", "42Paris!")


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)