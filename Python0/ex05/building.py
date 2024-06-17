import sys
import string
import re

def is_special(text):
    special_characters = [
        '|',   # Pipe
        '&',   # Ampersand
        ';',   # Semicolon
        '<',   # Redirection (input)
        '>',   # Redirection (output)
        '>>',  # Redirection (append)
        '&&',  # Logical AND
        '||',  # Logical OR
        '(',   # Parenthesis (open)
        ')',   # Parenthesis (close)
        '$',   # Dollar sign
        '`',   # Backtick
        '"',   # Double quote
        "'",   # Single quote
        '\\',  # Backslash
        '{',   # Curly brace (open)
        '}',   # Curly brace (close)
        '[',   # Square bracket (open)
        ']',   # Square bracket (close)
        '#',   # Hash (comment in shell)
        '*',   # Asterisk (wildcard)
        '?',   # Question mark (wildcard)
        '!',   # Exclamation mark (negation in shell, history expansion)
        '~'    # Tilde (home directory)
    ]
    if any(char in text for char in special_characters):
        print("The first argument starts with a special character")
        sys.exit(1)


def arg_check(args)->int:
    code = 0
    try:
        
        if len(args) < 2:
            code = 1
            return code
        is_special(args[1])
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

def message(text):
    print(f"\nThe text contains {str_len(text)} characters:")
    print(f"{upper_count(text)} upper letters")
    print(f"{lower_count(text)} lower letters")
    print(f"{punctuation_count(text)} punctuation marks")
    print(f"{space_count(text)} spaces")
    print(f"{digit_count(text)} digits")

def main():
    text = ""
    args = sys.argv
    er_code = arg_check(args)
    if er_code == 0:
        text = args[1]
    else:
        while text == "":
            print("What is the text to count?")
            try:
                text = sys.stdin.readline()           
                if not text:
                    text = ""
            except KeyboardInterrupt:
                print("\nKeyboard interrupt received. Ending Input.")
                sys.exit()
    if text:
        message(text)


if __name__== "__main__":
    main()