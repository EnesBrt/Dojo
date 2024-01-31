# Find the odd int

the_input = [0, 1, 0, 1, 0]


def find_it(seq):
    occurence = {}

    for n in the_input:
        if n in occurence:
            occurence[n] += 1
        else:
            occurence[n] = 1

    for key, value in occurence.items():
        if value % 2 != 0:
            return key


print(find_it(the_input))
