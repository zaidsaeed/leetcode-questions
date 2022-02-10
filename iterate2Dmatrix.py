# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
         ]

# \ -> this direction
def printTLBR(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Go through the first row
    for i in range(cols):
        x = 0 
        y = i
        diagonal = []
        while x < rows and y < cols:
            diagonal.append(matrix[x][y])
            x += 1
            y += 1
        print(diagonal)
        print('      ')
    
    # Go through the first column
    for j in range(1, rows):
        x = j
        y = 0
        diagonal = []
        while x < rows and y < cols:
            diagonal.append(matrix[x][y])
            x += 1
            y += 1
        print(diagonal)
        print('      ')

def printBRTL(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(cols):
        x = rows-1
        y = i
        diagonal = []
        while x > -1 and y > -1:
            diagonal.append(matrix[x][y])
            x -= 1
            y -= 1
        print(diagonal)
    for j in range(rows-1):
        x = j
        y = cols - 1
        diagonal = []
        while x > -1 and y > -1:
            diagonal.append(matrix[x][y])
            x -= 1
            y -= 1
        print(diagonal)
            
            
            
            
    
    

printBRTL(matrix)
# printTLBR(matrix)
