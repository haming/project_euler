import time
import numpy as np

def readAndTransform():
    fh = open('F:\project_euler\96 sudoku.txt')
    sudoku = np.zeros((9, 9), dtype=int)
    while fh.readline():
        for i in range(9):
            sudoku[i, :] = list(fh.readline().strip())
        yield sudoku

def solveSudoku(sudoku):
    if sudoku.all():
        return sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i,j] == 0:
#                print
#                print i,j
#                print sudoku
#                time.sleep(0.5)
                used = np.zeros(9, dtype=int)
#                print sudoku[i,sudoku[i,:].nonzero()]
                used[sudoku[i,sudoku[i,:].nonzero()]-1] = 1
#                print sudoku[sudoku[:,j].nonzero(),j]
                used[sudoku[sudoku[:,j].nonzero(),j]-1] = 1
                rows = np.arange(i//3*3,i//3*3+3)[:,np.newaxis]
                cols = np.arange(j//3*3,j//3*3+3).reshape((1,3))
                temp = sudoku[rows,cols]
#                print rows, cols
#                print temp[temp.nonzero()]
                used[temp[temp.nonzero()]-1] = 1
#                print used, np.where(used==0)[0]+1
                if used.all():
                    return False

                for num in np.where(used==0)[0]+1:
                    s = sudoku.copy()
                    s[i,j] = num
                    result = solveSudoku(s)
                    if type(result) != bool:
                        return result
#                    else:
#                        print 'bad'
                return False
    
total = 0
for sudoku in readAndTransform():
    total += solveSudoku(sudoku)[0,0:3].dot([100,10,1])
print total