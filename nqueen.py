n = int (input("Enter the value of n: "))

board = [[0 for i in range(n)]for i in range (n)]

# Initial State
print("Initial State: \n")
for row in board:
    print(row)

print("\n")

def check_column(board, row,column):
 
    for i in range(row, -1, -1):
        if board[i][column] == 1:
            return False
    
    return True

def check_diagonal(board, row, column):

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(column, n)):
        if board[i][j] == 1:
            return False
        
    return True

# Backtracking
def nqueen(board, row):
   
    if(row == n):
        return True  
    
    for i in range(n):
        if(check_column(board, row, i)== True and check_diagonal(board, row, i)== True):
            board[row][i] = 1
            if nqueen(board, row + 1):
                return True
            board[row][i] = 0

    return False

nqueen(board, 0)

# Final State
print("Final State: \n")
for row in board:
    print(row)