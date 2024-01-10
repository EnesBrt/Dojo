# find paire numbers

array = [1, 2, 3, 4, 3]
target = 6

tuples = []


def find_paires(arr, t):
    for n in range(len(arr) - 1):
        for x in range(n + 1, len(arr)):
            result = arr[n] + arr[x]
            if result == t:
                the_tuples = arr[n], arr[x]
                tuples.append(the_tuples)
    
        
    return tuples
    
        
print(find_paires(array, target))