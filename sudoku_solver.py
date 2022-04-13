import numpy as np

sudoku = [[0,0,0,6,0,0,0,0,0],
        [8,0,0,0,0,0,0,9,0],
        [0,3,0,0,5,2,0,0,4],
        [0,0,0,7,0,0,0,0,1],
        [3,0,0,0,6,1,8,0,0],
        [0,6,0,4,0,0,0,0,0],
        [0,5,0,0,1,3,0,0,2],
        [0,0,0,0,0,7,0,0,0],
        [0,0,2,0,0,0,4,0,0]]

# Tests whether or not the number z is a possible solution for the square[x][y]
def possible (x,y,z):
  global sudoku
  for i in range(0,9):
    if sudoku[x][i] == z:
      return False
  for i in range (0,9):
    if sudoku[i][y] == z:
      return False
  x0 = (x//3)*3
  y0 = (y//3)*3
  for i in range(0,3):
    for j in range(0,3):
      if sudoku[x0+i][y0+j] == z:
        return False
  return True

# Goes through every blank square and finds every solution possible
def solve():
  global sudoku
  for x in range(9):
    for y in range(9):
      if sudoku[x][y] == 0:
        for z in range(1,10):
          if possible(x,y,z):
            sudoku[x][y] = z
            solve()
            sudoku[x][y] = 0
        return
  print(np.matrix(sudoku))

solve()
