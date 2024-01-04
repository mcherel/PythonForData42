#!/usr/bin/env python3.10
# to execute:
# chmod +x NULL_not_found.py
# ./NULL_not_found.py

def NULL_not_found(obj: any=None) -> int:

    chars = ('\u2019', #right single quotation
             '\u2018', #right single quotation
             '\u0022', #double quotation
             '\u2028', #line separator
             '\u2029', #paragraph separator
             '\u0085', #next line
             '\u000C', #form feed
             '\u000B', #vertical tab
             '\u000A', #line feed
             '\u0009', #tab
             '\u0020', #space
            )
    try:
        match obj:
            case bool() if obj == False:  # case False              
                print(f"Fake: {obj} {type(obj)}")
                return 0
            case str() if all(char in chars for char in obj): #case empty ans right quote
                print(f"Empty: {type(obj)}")
                return 0
            case int() if not obj: #case 0             
                print(f"Zero: {obj} {type(obj)}")
                return 0
            case float() if obj != obj: #case nan               
                print(f"Cheese: {obj} {type(obj)}")
                return 0
            case None:  #case None           
                print(f"Nothing: {obj} {type(obj)}")
                return 0
            case _: #other cases
                print(f"Type not found")
                return 1

    except Exception as e:
        print(type(e))
        print(f"Exc : {type(e)}")
        return 0
