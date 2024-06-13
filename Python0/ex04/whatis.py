import sys

def whatlist():
    try:
        args = sys.argv

        assert len(args) > 1
        assert len(args) == 2, "more than one argument is provided" # assertion error : user declares a condition to be true
        num = args[1]
        assert num.lstrip('-').isnumeric(), "argument is not an integer"
        num = int(num)
        assert -sys.maxsize-1 <= num <= sys.maxsize, "argument is not an integer"

        response = "I'm Odd" if num % 2 else  "I'm Even"
        print(response)
        
    except AssertionError as er:
        if er.args:
            print(f'AssertionError: "{er}"')
    finally:
        print()

def main():
    whatlist()

if __name__== "__main__":
    main()