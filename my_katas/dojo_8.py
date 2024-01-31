# Stop gninnipS My sdroW!

the_input = input("write a sentence: ")


def spin_words(sentence):
    the_list = sentence.split()

    new_list = []

    for n in the_list:
        if len(n) >= 5:
            n = n[::-1]
            new_list.append(n)
        else:
            new_list.append(n)

        string_chain = " ".join(new_list)

    return string_chain


print(spin_words(the_input))
