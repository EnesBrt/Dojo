# Build Tower

the_input = int(input("Write a number: "))


def tower_builder(n_floors):
    tower = []
    max_length = 2 * n_floors - 1
    for n in range(n_floors):
        star = 2 * n + 1
        spaces = (max_length - star) // 2
        floor = " " * spaces + "*" * star + " " * spaces
        tower.append(floor)

    return tower


print(tower_builder(the_input))
