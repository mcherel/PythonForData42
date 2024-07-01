import sys


def arg_check(args) -> bool:
    try:
        assert len(args) == 2
        string = args[1]
        assert string.isalnum()
        return True

    except AssertionError:
        print('AssertionError: the arguments are bad')
        sys.exit()


def morse_converter(msg: str):
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
    return [morse_code_dict[i] for i in msg]


def main():
    args = sys.argv
    if arg_check(args):
        print(" ".join(morse_converter(str(args[1]).upper())))


if __name__ == "__main__":
    main()
