import sys

def whatlist():
    try:
        args = sys.argv
        assert len(args) == 2, "more than one argument is provided" # assertion error : user declares a condition to be true
        #print(args[1].isnumeric())
        #print(-sys.maxsize-1)
        num = args[1]
        assert num.lstrip('-').isnumeric(), "argument is not an integer"
        num = int(num)
        assert -sys.maxsize-1 <= num <= sys.maxsize, "argument is not an integer"
        #print(num)
        #print(type(num))
    except AssertionError as er:
        print(f'AssertionError: "{er}"')
whatlist()