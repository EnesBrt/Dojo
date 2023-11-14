# Which are in?

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]


def in_array(array1, array2):
    result = []
    for word1 in array1:
        for word2 in array2:
            if word1 in word2 and word1 not in result:
                result.append(word1)
                break
    return sorted(result)


test = in_array(a1, a2)
print(test)
