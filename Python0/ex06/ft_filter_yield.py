import typing


def ft_filter(*args: typing.Any):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    try:
        print(len(args))
        if len(args) != 2:
            raise TypeError
        else:
            f, i = args
            if f is None:
                for item in (r for r in i if r):
                    yield item
                return
            for item in (r for r in i if f(r)):
                yield item
    except TypeError as err:
        if len(args) != 2:
            print(f"TypeError: filter expected 2 arguments, got {len(args)}")
        else:
            print(f"{type(err).__name__}: {err}")
        exit(1)
