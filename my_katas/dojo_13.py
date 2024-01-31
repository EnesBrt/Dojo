# Persistent Bugger

the_input = input("write a number: ")


def persistence(n):
    the_list = [int(i) for i in n]
    result = 1

    if len(n) == 1:
        return 0

    for i in the_list:
        result = i * result

    return 1 + persistence(str(result))


print(persistence(the_input))
