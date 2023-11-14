the_input = input("write something: ")


def valid_braces(string):
    pile = []
    matching_braces = {")": "(", "]": "[", "}": "{"}

    for n in string:
        if n in ["(", "[", "{"]:
            pile.append(n)
        elif n in [")", "]", "}"]:
            if not pile:
                return False
            last_element = pile.pop()
            if matching_braces[n] != last_element:
                return False

    return not pile


print(valid_braces(the_input))
