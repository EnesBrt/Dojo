# Rotate array

array = [1, 2, 3, 4, 5]

def rotate(arr, number):
    
    arr = arr[number:] + arr[:number]
    
    return arr
        
print(rotate(array, 1))
