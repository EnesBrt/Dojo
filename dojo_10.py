# Sum of Digits / Digital Root

the_input = int(input("write a number: "))


def digital_root(n):
    the_list = str(n)
    the_list = [int(i) for i in the_list]
    result = 0

    for i in the_list:
        result = i + result

    if len(str(result)) >= 2:
        result = digital_root(result)

    return result


print(digital_root(the_input))
