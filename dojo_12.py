# Equal Sides Of An Array

the_input = list(range(-1, -100))


def find_even_index(arr):
    if 0 < len(arr) < 1000:
        for n in range(len(arr)):
            left = sum(arr[0:n])
            right = sum(arr[n + 1 :])
            if left == right:
                return n
        return -1
    else:
        return -1


print(find_even_index(the_input))
