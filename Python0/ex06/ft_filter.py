import sys

def ft_filter(*args):
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
class Filter:
    def __init__(self, function, iterable):
        """
        Initialize the filter object with a function and an iterable.
        
        Args:
            function: A function that returns True or False for each item in the iterable.
            iterable: An iterable whose items are to be filtered.
        """
        self.function = function
        self.iterable = iterable

    def __iter__(self):
        """
        Return an iterator that yields items from the iterable for which the function returns True.
        
        Yields:
            Items from the iterable for which the function returns True.
        """
        return self._filter_generator()

    def _filter_generator(self):
        """
        Generator that yields items from the iterable for which the function returns True.
        
        Yields:
            Items from the iterable for which the function returns True.
        """
        for item in self.iterable:
            if self.function(item):
                yield item

# Example usage
def is_alpha(item):
    """Return True if the item is a non-empty string containing only alphabetic characters."""
    return isinstance(item, str) and item.isalpha()

# Test data
data = ["Hello", "123", "World!", "Python", "", None, True]

# Create a Filter object
filtered_data = Filter(is_alpha, data)

# Convert the Filter object to a list to see the result
filtered_list = list(filtered_data)
print(filtered_list)  # Output: ['Hello', 'Python']

'''
        

