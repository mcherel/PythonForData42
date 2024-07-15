
import sys
import shutil


def ft_tqdm(lst: range) -> None:  # type: ignore
    """
    Mimic the behavior of tqdm progress bar for an iterable.

    Args:
        lst (range): The iterable (range) to iterate over with a progress bar.

    Yields:
        int: The items from the iterable `lst`, one at a time.
    """
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        columns = shutil.get_terminal_size().columns
        bar_length = columns - 40 if columns > 40 else 10
        percent = int((i / total) * 100)
        filled_length = int((i / total) * bar_length) - 3
        filled_print = '=' * filled_length + ">"
        not_filled_print = ' ' * (bar_length - filled_length - 3)
        bar = filled_print + not_filled_print
        sys.stdout.write(f'\r{percent}%|[{bar}]| {i}/{total}')
        sys.stdout.flush()
        yield item

    sys.stdout.write('\n')
    return None
