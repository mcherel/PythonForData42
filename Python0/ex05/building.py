import sys
import string

def arg_check(args)->int:
    code = 0
    try:
        
        if len(args) < 2:
            code = 1
            return code
        assert len(args) == 2, "more than one argument is provided"    
    except AssertionError as er:
        code = 1
        if er.args:
            print(f'AssertionError: "{er}"')
            sys.exit()
    finally:
        return code  

def str_len(s)->int:
    return len(s)

def upper_count(s)->int:
    return(sum([1 for i in s if i.isupper()]))

def lower_count(s)->int:
    return(sum([1 for i in s if i.islower()]))

def punctuation_count(s)->int:
    return(sum([1 for i in s if i in string.punctuation]))

def space_count(s)->int:
    return(sum([1 for i in s if i.isspace()]))

def digit_count(s)->int:
    return(sum([1 for i in s if i.isdigit()]))

def message(text, space, str_l):
    print(f"The text contains {str_l} characters:")
    print(f"{upper_count(text)} upper letters")
    print(f"{lower_count(text)} lower letters")
    print(f"{punctuation_count(text)} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit_count(text)} digits")

def main():
    space = str_l =0
    text = ""
    args = sys.argv
    er_code = arg_check(args)
    print("Error code : " + str(er_code))
    if er_code == 0:
        text = args[1]
        space = space_count(text)
        str_l = str_len(text)
    else:
        while not text:
            try:
                text = input("What is the text to count?\n")
                space = space_count(text) + 1
                str_l = str_len(text) + 1
            except EOFError:
                space = space_count(text)
                str_l = str_len(text)
                message(text, space, str_l)
                break

    message(text, space, str_l)


if __name__== "__main__":
    main()

"""
import sys
import string

def arg_check(args) -> int:
    code = 0
    try:
        if len(args) < 2:
            code = 1
            return code
        assert len(args) == 2, "More than one argument is provided"
    except AssertionError as er:
        code = 1
        if er.args:
            print(f'AssertionError: "{er}"')
            sys.exit()
    finally:
        return code

def str_len(s) -> int:
    return len(s)

def upper_count(s) -> int:
    return sum(1 for i in s if i.isupper())

def lower_count(s) -> int:
    return sum(1 for i in s if i.islower())

def punctuation_count(s) -> int:
    return sum(1 for i in s if i in string.punctuation)

def space_count(s) -> int:
    return sum(1 for i in s if i.isspace())

def digit_count(s) -> int:
    return sum(1 for i in s if i.isdigit())

def message(text, space, str_l):
    print(f"The text contains {str_l} characters:")
    print(f"{upper_count(text)} upper letters")
    print(f"{lower_count(text)} lower letters")
    print(f"{punctuation_count(text)} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit_count(text)} digits")

def main():
    space = str_l = 0
    text = ""
    args = sys.argv
    er_code = arg_check(args)
    print("Error code: " + str(er_code))
    if er_code == 0:
        text = args[1]
        space = space_count(text)
        str_l = str_len(text)
    else:
        try:
            while not text:
                try:
                    text = input("What is the text to count?\n")
                    if text:
                        space = space_count(text)
                        str_l = str_len(text)
                except EOFError:
                    print("\nEOF received. Ending input.")
                    break
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received. Ending input.")
            sys.exit()

    if text:  # Only display the message if text is not empty
        message(text, space, str_l)

if __name__ == "__main__":
    main()

"""