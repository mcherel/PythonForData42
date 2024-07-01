import ft_filter as f
import sys

def arg_check(args) -> bool:
    try:
        
        assert len(args) == 3, "the arguments are bad" # assertion error : user declares a condition to be true
        string = args[1]
        for s in string.split():
          assert s.isalnum(), "argument is not an alphanumerical character"
        num = args[2]
        assert num.isnumeric(), "argument is not a positive integer"
        assert -sys.maxsize-1 <= int(num) <= sys.maxsize, "argument is not an integer"
        
        return True
        
    except AssertionError as er:
        if er.args:
            print(f'AssertionError: "{er}"')
            sys.exit()

def main():
    args = sys.argv
    print(arg_check(args))

if __name__== "__main__":
    main()