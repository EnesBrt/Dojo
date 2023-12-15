# Build Tower

the_input = int(input("Write a number: "))


def tower_builder(n_floors):
    tower = []
    i = 1
    max_length = 2 * n_floors - 1
    for n in range(n_floors + 1):
        star = 2 * i + 1
        i += 1
        spaces = (max_length - star) // 2
        floor = " " * spaces + "*" * star + " " * spaces
        tower.append(floor)

    return tower


print(tower_builder(the_input))
