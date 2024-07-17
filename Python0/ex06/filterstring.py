import sys
import ft_filter as f


def arg_check(args) -> bool:
    """
    Checks if the command line arguments are valid.

    Parameters:
    args (list): List of command line arguments.

    Returns:
    bool: True if arguments are valid, otherwise exits the program.
    """
    try:
        # Check if there are exactly 3 arguments
        assert len(args) == 3

        # Check if the first argument is a string of alphanumeric words
        string = args[1]
        assert all([s.isalnum() for s in string.split()])

        # Check if the second argument is an integer
        num = args[2]
        assert num.isnumeric()
        assert -sys.maxsize-1 <= int(num) <= sys.maxsize

        return True

    except AssertionError:
        # Print error message and exit if any assertion fails
        print('AssertionError: the arguments are bad')
        sys.exit()


def main():
    """
    Main function to execute the script.
    """
    # Get the command line arguments
    args = sys.argv

    # Check if arguments are valid
    if arg_check(args):
        # Split the first argument into words
        words = args[1].split()

        # Convert the second argument to an integer
        num = int(args[2])

        # Use ft_filter to filter words longer than the given number
        print(f.ft_filter(lambda word: len(word) > num, words))


if __name__ == "__main__":
    # Execute main function if script is run directly
    main()
