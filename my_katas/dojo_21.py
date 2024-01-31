# counting sort

def countingSort(arr):
    # Trouver la valeur maximale dans le tableau pour déterminer la taille du tableau de décompte
    max_val = max(arr)

    # Initialiser le tableau de décompte avec des zéros
    count_array = [0] * (max_val + 1)

    # Étape 1 : Compter les occurrences
    for num in arr:
        count_array[num] += 1

    # Étape 2 : Calculer les positions cumulatives
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # Étape 3 : Placer les éléments dans le tableau trié
    sorted_array = [0] * len(arr)
    for num in reversed(arr):
        count_array[num] -= 1
        sorted_array[count_array[num]] = num

    return sorted_array

# Exemple d'utilisation
input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = countingSort(input_array)
print("Tableau trié :", sorted_array)
