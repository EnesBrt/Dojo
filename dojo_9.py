# Who likes it?

the_input = []


def likes(names):
    if not names or all(name.strip() == "" for name in names):
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} likes this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} likes this"
    elif len(names) >= 4:
        remaining_length = len(names) - 2
        return f"{names[0]}, {names[1]} and {remaining_length} others likes this"
    elif names[n] == " ":
        return "no one likes this"


print(likes(the_input))
