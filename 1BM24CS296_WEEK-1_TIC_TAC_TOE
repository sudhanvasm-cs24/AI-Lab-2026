import random

grid = [[" " for _ in range(3)] for _ in range (3)]

def display_grid():
  for i in range(3):
    for j in range(3):
      print(grid[i][j], end=" | ")
    print("\n--+---+---+--")

def check_win(symbol):
  if ((grid[0][0] == grid[0][1] == grid[0][2] == symbol) or
      (grid[1][0] == grid[1][1] == grid[1][2] == symbol) or
      (grid[2][0] == grid[2][1] == grid[2][2] == symbol) or
      (grid[0][0] == grid[1][0] == grid[2][0] == symbol) or
      (grid[0][1] == grid[1][1] == grid[2][1] == symbol) or
      (grid[0][2] == grid[1][2] == grid[2][2] == symbol) or
      (grid[0][0] == grid[1][1] == grid[2][2] == symbol) or
      (grid[2][2] == grid[1][1] == grid[0][2] == symbol)):
      return True
  return False

def check_tie():
  for i in range(3):
    for j in range(3):
      if grid[i][j] == " ":
        return False
  return True
    
while True:
  display_grid()

  r, c = input("Enter row and column (e.g., 1 2): ").split()
  r, c = int(r), int(c)
  grid[r][c] = "X"
  if check_win("X"):
    display_grid()
    print("Player Wins.\n")
    break

  while grid[r][c] != " ":
    r, c = random.randint(0, 2), random.randint(0, 2)

  grid[r][c] = "O"
  
  if check_win("O"):
    display_grid()
    print("Computer Wins.\n")
    break

  if check_tie():
    display_grid()
    print("Draw.\n")
    break
