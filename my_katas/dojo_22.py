"""fonction compte la fréquence de chaque nombre de 0 à 99 dans le tableau arr 
et retourne un tableau de fréquence de taille 100."""

def countingSort(arr):
    # Initialiser un tableau de fréquence de taille 100
    frequency = [0] * 100

    # Compter les occurrences de chaque nombre dans arr
    for num in arr:
        frequency[num] += 1

    return frequency

# Exemple d'utilisation
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
