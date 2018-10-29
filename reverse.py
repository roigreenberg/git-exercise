def print_odd(org: list):
    odd = org[0::2]
    print(odd)


def print_reverse(org: list):
    new_list = org[0:len(org):-1]

    print(new_list)


if __name__ == '__main__':
    print_reverse(list(range(10)))

