# Create Phone Number

the_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def create_phone_number(n):
    numbers = [str(x) for x in n]
    numbers = "".join(numbers)
    return f"({numbers[0:3]}) {numbers[3:6]}-{numbers[6:10]}"


print(create_phone_number(the_input))
