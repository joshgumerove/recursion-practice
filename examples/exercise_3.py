# Parameters:
#  matrix: List[List[int]]
# return type: int

def minimumCostPath(matrix, i = 0, j = 0):
    return matrix[i][j] + min(minimumCostPath(matrix, i + 1, j), minimumCostPath(matrix, i, j + 1))

matrx = [[3, 12, 4, 7, 10], [6, 8, 15, 11, 4], [19, 5, 14, 32, 21], [1, 20, 2, 9, 7]]

# note solution in video

def phrases(arr, i = 0):
    if i >= len(arr) -1:
        return arr
    for phrases in arr:
        return phrases[i] + arr[i + i][i]
    
    
    

phrase = [
    ['I', 'You', 'They'], 
    ['love', 'hate'], 
    ['food', 'games']
    ]

print(phrases(phrase))