
def pattern_print(n):
    num_rows = int((2 * n-1) ** 0.5)

    for i in range(1, num_rows + 1):
        print(' ' * (num_rows - i), '* ' * i)


def input_your_string(given_stars):
    n = len(given_stars.replace(" ", ""))
    pattern_print(n)
