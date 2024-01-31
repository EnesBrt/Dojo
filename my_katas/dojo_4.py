# Multiples of 3 or 5


def sum_of_multiples(limit):
    if limit < 0:
        return 0
    total = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# Example usage
number = 20
result = sum_of_multiples(number)
print(f"Sum of multiples of 3 or 5 below {number} is {result}")
