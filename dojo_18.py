# Sparse Arrays

string = ["ab", "ab", "abc"]
query = ["ab", "abc", "bc"]


def matchingStrings(queries, strings):
    dictionary = {}

    # Initialiser le dictionnaire avec des clés de 'queries' et des compteurs à 0
    for query in queries:
        dictionary[query] = 0

    # Parcourir la liste 'strings' et incrémenter le compteur pour chaque correspondance
    for string in strings:
        if string in dictionary:
            dictionary[string] += 1

    # Récupérer les compteurs dans l'ordre des requêtes
    new_list = [dictionary[query] for query in queries]

    return new_list


print(matchingStrings(query, string))
