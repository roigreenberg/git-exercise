def reverse(org: list):
    new_list = org[0:len(org):-1]

    print(new_list)


if __name__ == '__main__':
    reverse(list(range(10)))

