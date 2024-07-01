import sys


def arg_check(args) -> bool:
    try:
        assert len(args) == 3
        string = args[1]
        for s in string.split():
            assert s.isalnum()
        num = args[2]
        assert num.isnumeric()
        assert -sys.maxsize-1 <= int(num) <= sys.maxsize
        return True

    except AssertionError:
        print('AssertionError: the arguments are bad')
        sys.exit()


def ft_list(num):
    return lambda words: [i for i in words if len(i) > num]


def main():
    args = sys.argv
    if arg_check(args):
        words = args[1].split()
        num = int(args[2])
        ft_checker = ft_list(num)
        print(ft_checker(words))


if __name__ == "__main__":
    main()
