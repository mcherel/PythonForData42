#!/usr/bin/env python3.10
# to execute:
# chmod +x Hello.py
# ./Hello.py

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = 'World'
ft_tuple = ("Hello", "France!")
ft_set = set(("Hello", "Paris!"))
ft_dict["Hello"] = '42Paris'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
