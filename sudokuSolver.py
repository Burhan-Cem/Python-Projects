#! python3

def solveTim(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i 
            if solveTim(bo):
                return True
            bo[row][col] = 0
    return False

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if not bo[i][j]:
                return (i, j) #  row, col
def valid(bo, num, pos):
    # Check row
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check 3*3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(bo):
    for i in range(9):
        if i % 3 == 0:
            print('+ - - - + - - - + - - - +')
        for j in range(9):
            if j % 3 == 0:
                print('| ', end='')
                
            if j == 8:
                print(bo[i][j], '|')
            else:
                print(str(bo[i][j]) + ' ', end='')
    print('+ - - - + - - - + - - - +\n')
    




def solvePhil():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        board[y][x] = n
                        solvePhil()
                        board[y][x] = 0 
                return
    print_board(board)
    input('More?')

def possible(y,x,n):
    global board
    for i in range(9):
        if board[y][i] == n:
            return False
    for i in range(9):
        if board[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[y0+i][x0+j] == n:
                return False
    return True

#------------------------------------------------------#
board = [[0,0,0,0,0,9,0,7,0],
         [0,0,0,0,8,2,0,5,0],
         [3,2,7,0,0,0,0,4,0],
         [0,1,6,0,4,0,0,0,0],
         [0,5,0,0,0,0,3,0,0],
         [0,0,0,0,9,0,7,0,0],
         [0,0,0,6,0,0,0,0,5],
         [8,0,2,0,0,0,0,0,0],
         [0,0,4,2,0,0,0,0,8]]

print_board(board)
#solveTim(board)
#solvePhil()
print_board(board)
    
