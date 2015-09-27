import numpy as np

def readAndTransform():
    fh = open('F:\project_euler\96 sudoku.txt')
    sudoku = np.zeros((9, 9), dtype=int)
    while fh.readline():
        for i in range(9):
            sudoku[i, :] = list(fh.readline().strip())
        yield sudoku

#def possibilities(sudoku, i, j):
#    used = np.zeros(9, dtype=int)
#    used[sudoku[i,sudoku[i,:].nonzero()]-1] = 1
#    used[sudoku[sudoku[:,j].nonzero(),j]-1] = 1
#    rows = np.arange(i//3*3,i//3*3+3)[:,np.newaxis]
#    cols = np.arange(j//3*3,j//3*3+3).reshape((1,3))
#    temp = sudoku[rows,cols]
#    used[temp[temp.nonzero()]-1] = 1
#    
#    return np.where(used==0)[0]+1

def possibilities(sudoku, i, j):
    s = set()
    rowStart, colStart = i-i%3, j-j%3
    for r in range(3):
        for c in range(3):
            s.add(sudoku[rowStart+r, colStart+c])
    s.update(sudoku[i,:])
    s.update(sudoku[:,j])
    
    return set([1,2,3,4,5,6,7,8,9])-s

def solveSudoku(sudoku, i=0, j=0):
#    print sudoku
    while sudoku[i,j]:
        i += 1
        if i == 9:
            i, j = 0, j+1
        if j == 9:
            return True

    for num in possibilities(sudoku, i, j):
        sudoku[i,j] = num
        if solveSudoku(sudoku, i, j):
            return True
    sudoku[i,j] = 0
    return False
    
total = 0
for sudoku in readAndTransform():
#    print sudoku
    solveSudoku(sudoku)
    total += sudoku[0,0:3].dot([100,10,1])
print total