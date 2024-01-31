# Subarray Division

chocolate = [1, 2, 1, 3, 2]
day = 3
month = 2

def birthday(s, d, m):
    
    sums = []
    
    for i in range(len(s) - m + 1):
        # Initialiser la somme pour la sous-liste courante
        current_sum = 0
        # Boucle pour additionner n éléments consécutifs
        for j in range(i, i + m):
            current_sum += s[j]
    
        # Ajouter la somme calculée à la liste des sommes
        if current_sum == d:
            sums.append(current_sum)
        
    occurence = {}
    for i in sums:
        if i in occurence:
            occurence[i] += 1
        else:
            occurence[i] = 1
            
    maximum = 0
    for key, value in occurence.items():
        if value > maximum:
            maximum = value
    
    return maximum
    
print(birthday(chocolate, day, month))
    