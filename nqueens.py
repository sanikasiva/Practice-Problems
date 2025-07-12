k = int(input("Enter the number of queens: "))
chessboard = [[0] * k for _ in range(k)]

def isAttacking(row, col):
    # Row-wise
    for c in range(k):
        if chessboard[row][c] == 1:
            return True

    # Column-wise
    for r in range(k):
        if chessboard[r][col] == 1:
            return True
    #diagonal
    diff = row - col
    for r in range(k):
        c = r - diff
        if 0 <= c < k and chessboard[r][c] == 1:
            return True

    #diagonal 2
    add = row + col
    for r in range(k):
        c = add - r
        if 0 <= c < k and chessboard[r][c] == 1:
            return True

    return False

def nQueens(x):
    if x == 0:
        return True
        
    for i in range(k):
        for j in range(k):
            if chessboard[i][j] == 0 and not isAttacking(i, j):
                chessboard[i][j] = 1
                if nQueens(x - 1):
                    return True
                chessboard[i][j] = 0

    return False

if nQueens(k):
    print("True")
else:
    print("No solution")
        
    
    
