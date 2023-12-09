# Find the unique number

array = [3, 10, 3, 3, 3]


def find_uniq(arr):
    list_one = []
    list_two = []

    # list_one.append(arr[0])
    for n in arr:
        if n == arr[0]:
            list_one.append(n)
        else:
            list_two.append(n)

    if len(list_one) > len(list_two):
        return float(" ".join(str(i) for i in list_two))
    else:
        return float(" ".join(str(i) for i in list_one))


print(find_uniq(array))
