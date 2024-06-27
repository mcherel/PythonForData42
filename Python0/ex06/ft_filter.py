import sys

def ft_filter(f: bool=None, i: list=None):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    try:
        return [r for r in i if f(r)]
    except TypeError as err:
        args = sum((1 for j in [f, i] if j != None))
        print(args)
        if args != 2:
            print(f"TypeError: filter expected 2 arguments, got {args}")
            exit(1)
        print(f"{type(err).__name__}: {err}")
        

