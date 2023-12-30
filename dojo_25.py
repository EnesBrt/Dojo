# fliping matrix

the_matrix = [
    [1, 2, 9, 10],
    [3, 4, 11, 12],
    [5, 6, 13, 14],
    [7, 8, 15, 16]
]

"""
Position Originale : (i, j)
Symétrie Horizontale : (i, 2n-1-j)
Symétrie Verticale : (2n-1-i, j)
Symétrie Diagonale : (2n-1-i, 2n-1-j)
"""




def flip_matrix(matrix):
    n = len(matrix) // 2 
    total = 0
    for i in range(n):
        for j in range(n):
            max_value = max(matrix[i][j], 
            matrix[i][2*n-1-j], 
            matrix[2*n-1-i][j], 
            matrix[2*n-1-i][2*n-1-j])

            total += max_value
                
    return total
    
print(flip_matrix(the_matrix))