import sys


def arg_check(args) -> bool:
    """
    Checks if the command line arguments are valid.

    Parameters:
    args (list): List of command line arguments.

    Returns:
    bool: True if arguments are valid, otherwise exits the program.
    """
    try:
        assert len(args) == 2
        string = args[1]
        assert string.isalnum()
        return True

    except AssertionError:
        print('AssertionError: the arguments are bad')
        sys.exit()


def morse_converter(msg: str) -> str:
    """
    Translates the alphanum message into morse.

    Parameters:
    args (string): Message to translate.

    Returns:
    str: Translated message.
    """
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    return " ".join([morse_code_dict[i] for i in msg])


def main():
    args = sys.argv
    if arg_check(args):
        print(morse_converter(str(args[1]).upper()))


if __name__ == "__main__":
    main()
