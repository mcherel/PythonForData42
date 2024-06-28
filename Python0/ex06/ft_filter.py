import typing

def ft_filter(*args: typing.Any) -> typing.List[typing.Any]:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    try:
        if len(args) != 2:
            raise TypeError
        f, i = args
        if f == None:
            return [r for r in i]
        return [r for r in i if f(r)]
    except TypeError as err:
        if len(args) != 2:
            print(f"TypeError: filter expected 2 arguments, got {len(args)}")
            exit(1)
        print(f"{type(err).__name__}: {err}")
        exit(1)
'''
from typing import Any, Callable, List, Tuple, overload

@overload
def my_function(func: Callable[[Any], Any], lst: List[Any]) -> None: ...
@overload
def my_function(func: Callable[[Any], Any], lst: List[Any], *args: Tuple[Any]) -> None: ...

def my_function(func: Callable[[Any], Any], lst: List[Any], *args: Any) -> None:
    print(f"Function: {func.__name__}")
    print(f"List: {lst}")
    print(f"Additional arguments: {args}")

    if len(args) == 0:
        print("No additional arguments.")
    elif len(args) == 1:
        print(f"One additional argument: {args[0]}")
    elif len(args) > 1:
        print(f"More than one additional argument: {args}")

    # Example: Applying the function to each element in the list
    results = [func(item) for item in lst]
    print(f"Results: {results}")

# Example usage
def example_func(x: int) -> int:
    return x * 2

my_list = [1, 2, 3, 4]

# Calling with no additional arguments
my_function(example_func, my_list)

# Calling with one additional argument
my_function(example_func, my_list, "extra_arg1")

# Calling with more than one additional argument
my_function(example_func, my_list, "extra_arg1", "extra_arg2")

'''
        

