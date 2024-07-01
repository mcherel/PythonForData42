import sys
import ft_filter as f


def arg_check(args) -> bool:
    try:
        assert len(args) == 3
        string = args[1]
        assert all([s.isalnum() for s in string.split()])
        num = args[2]
        assert num.isnumeric()
        assert -sys.maxsize-1 <= int(num) <= sys.maxsize
        return True

    except AssertionError:
        print('AssertionError: the arguments are bad')
        sys.exit()


def main():
    args = sys.argv
    if arg_check(args):
        words = args[1].split()
        num = int(args[2])
        print(f.ft_filter(lambda word: len(word) > num, words))


if __name__ == "__main__":
    main()
