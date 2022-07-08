from time import time


def ft_progress(lst):
    start = time()
    for i in lst:
        div = i / len(lst)
        delta = time() - start
        eta = 0
        if div:
            eta = delta / div - delta
        print('\rETA: {0:.2f}s'.format(eta), '[{:3.0f}%]'.format(div * 100), end=' ')  # % part
        bar = (("=" * (round(div * 40) - 1)) + ">").ljust(40)
        print('[{:40s}]'.format(bar), i + 1, '/', len(lst), '| elapsed time {0:.2f}s'.format(delta), end='')  # stat part
        yield lst[i]
