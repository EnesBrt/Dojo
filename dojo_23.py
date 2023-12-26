# Valid permutations

A = [2, 1, 3]
B = [7, 8, 9]
k = 10
 
def twoArrays(k, Arr, Brr):
    Arr = sorted(A)
    Brr = sorted(B, reverse=True)
     
    for n in range(len(A)):
        if Arr[n] + Brr[n] < k:
            return "NO"
            
    return "YES"
     
print(twoArrays(k, A, B))
