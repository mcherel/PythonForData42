import os
import sys
import string  # Needed for string.punctuation


def block_pipes():
    """
    Function to block execution if input/output is redirected or piped.

    This function checks if the standard input, output, and error streams
    are connected to a terminal. If any of them are not, it prints an error
    message and exits the program with a status code of 1.
    """
    if not (os.isatty(sys.stdin.fileno()) and
            os.isatty(sys.stdout.fileno()) and
            os.isatty(sys.stderr.fileno())):
        print("Pipes or redirections are not allowed.", file=sys.stderr)
        sys.exit(1)


def arg_check(args) -> int:
    """
    Function to check command-line arguments.

    Args:
        args: List of command-line arguments.

    Returns:
        An integer code representing the status of the argument check.
        Returns 1 if there is an assertion error, otherwise 0.
    """
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


def str_len(s) -> int:
    """
    Function to return the length of the string.

    Args:
        s: The input string.

    Returns:
        The length of the input string.
    """
    return len(s)


def upper_count(s) -> int:
    """
    Function to count the number of uppercase letters in the string.

    Args:
        s: The input string.

    Returns:
        The count of uppercase letters in the input string.
    """
    return sum([1 for i in s if i.isupper()])


def lower_count(s) -> int:
    """
    Function to count the number of lowercase letters in the string.

    Args:
        s: The input string.

    Returns:
        The count of lowercase letters in the input string.
    """
    return sum([1 for i in s if i.islower()])


def punctuation_count(s) -> int:
    """
    Function to count the number of punctuation marks in the string.

    Args:
        s: The input string.

    Returns:
        The count of punctuation marks in the input string.
    """
    return sum([1 for i in s if i in string.punctuation])


def space_count(s) -> int:
    """
    Function to count the number of spaces in the string.

    Args:
        s: The input string.

    Returns:
        The count of spaces in the input string.
    """
    return sum([1 for i in s if i.isspace()])


def digit_count(s) -> int:
    """
    Function to count the number of digits in the string.

    Args:
        s: The input string.

    Returns:
        The count of digits in the input string.
    """
    return sum([1 for i in s if i.isdigit()])


def message(text):
    """
    Function to print the analysis of the text.

    Args:
        text: The input text to be analyzed.

    This function prints the length of the text and counts of uppercase
    letters, lowercase letters, punctuation marks, spaces, and digits.
    """
    print(f"\nThe text contains {str_len(text)} characters:")
    print(f"{upper_count(text)} upper letters")
    print(f"{lower_count(text)} lower letters")
    print(f"{punctuation_count(text)} punctuation marks")
    print(f"{space_count(text)} spaces")
    print(f"{digit_count(text)} digits")


def main():
    """
    Main function to block pipes, check arguments, and analyze text.

    This function first calls block_pipes() to ensure the program is not
    run with pipes or redirections. It then checks the command-line arguments
    with arg_check() and reads the text input from either the arguments or
    stdin. Finally, it calls message() to print the analysis of the text.
    """
    block_pipes()  # Ensure the program is not run with pipes or redirections
    text = ""
    args = sys.argv
    er_code = arg_check(args)  # Check the command-line arguments

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
                sys.exit(1)
            finally:
                pass
    if text:
        message(text)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except BrokenPipeError:
            pass
        sys.exit(1)
