# Find the médiane


def calculer_mediane(data):
    # Trier l'ensemble des données
    data = sorted(data)

    # Calculer la médiane
    n = len(data)
    mid = n // 2

    if n % 2 == 0:  # Si le nombre d'éléments est pair
        # La médiane est la moyenne des deux valeurs centrales
        return (data[mid - 1] + data[mid]) / 2
    else:  # Si le nombre d'éléments est impair
        # La médiane est l'élément au milieu
        return data[mid]


# Exemple d'utilisation
data_impair = [3, 1, 9, 7, 3, 6, 8]
data_pair = [1, 2, 3, 4, 5, 6, 8, 9]

print(
    "Médiane (impair):", calculer_mediane(data_impair)
)  # Exemple avec un nombre impair d'éléments
print(
    "Médiane (pair):", calculer_mediane(data_pair)
)  # Exemple avec un nombre pair d'éléments
