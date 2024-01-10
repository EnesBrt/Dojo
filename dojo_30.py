# Minimisation de l'Injustice

array = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]


def maxMin(k, arr):
    
    arr.sort()
    min_unfairness = float('inf')
    
    for n in range(len(arr) - k + 1):
        current_unfairness = arr[n + k - 1] - arr[n]
        
        if current_unfairness < min_unfairness:
            min_unfairness = current_unfairness
            
    return min_unfairness
    

print(maxMin(4, array))
