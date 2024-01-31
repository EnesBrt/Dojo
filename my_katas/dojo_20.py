# diagonalDifference

def diagonalDifference(arr):
    n = len(arr)
    somme_gauche_droite = 0
    somme_droite_gauche = 0

    for i in range(n):
        somme_gauche_droite += arr[i][i]
        somme_droite_gauche += arr[i][n - 1 - i]
    
    absolute_result = abs(somme_gauche_droite - somme_droite_gauche)
    
    return (absolute_result)