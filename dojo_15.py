# Array.diff

first_list = [1, 2, 3]
second_list = [1, 2]


def array_diff(a, b):
    new_list = []

    for n in a:
        if n not in b:
            new_list.append(n)

    return new_list


print(array_diff(first_list, second_list))
