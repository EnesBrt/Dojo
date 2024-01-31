# Sous-ensemble le Plus Proche

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
taille_sous_ensemble = 3
target = 31

def find_closer_subs(arr, k, t):
    
    sums_array = []
    for n in range(len(arr) - k + 1):
        sums = 0
        for x in range(n, n + k):
            sums = arr[x] + sums
        sums_array.append(sums)
    
    closest_element = None
    min_diff = float('inf')

    for element in sums_array:
        diff = abs(element - target)
        if diff < min_diff:
            closest_element = element
            min_diff = diff

    return closest_element
        
    
print(find_closer_subs(array, taille_sous_ensemble, target))
