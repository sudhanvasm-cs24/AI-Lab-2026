import random

def tic_tac_toe(): 
  grid = [[" " for _ in range(3)] for _ in range(3)]
  
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
          (grid[0][2] == grid[1][1] == grid[2][0] == symbol)):
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
  
      if r not in range(3) or c not in range(3) or grid[r][c] != " ":
          print("Invalid move. Try again.")
          continue
  
      grid[r][c] = "X"
  
      if check_win("X"):
          display_grid()
          print("Player Wins.\n")
          break
  
      if check_tie():
          display_grid()
          print("Draw.\n")
          break
  
      while True:
          r, c = random.randint(0, 2), random.randint(0, 2)
          if grid[r][c] == " ":
              break
  
      grid[r][c] = "O"
  
      if check_win("O"):
          display_grid()
          print("Computer Wins.\n")
          break
  
      if check_tie():
          display_grid()
          print("Draw.\n")
          break

def vacuum_cleaner():
  grid = [[" " for _ in range(2)] for _ in range(2)]
  
  def display_grid():
      for i in range(2):
          for j in range(2):
              print(grid[i][j], end=" | ")
          print("\n--+---+--")
  
  for i in range(2):
      grid[1][i] = "D"
  
  grid[0][0] = "V"
  
  display_grid()
  
  while "D" in grid[1]:
  
      if grid[1][0] == "D":
          print("Room A is dirty. Cleaning Room A.")
          grid[1][0] = " "
          print("Moving to Room B")
      else:
          print("Room A is clean. Moving to Room B.")
          grid[0][1] = "V"
  
      if grid[1][1] == "D":
          print("Room B is dirty. Cleaning Room B.")
  
          if grid[1][0] != " ":
              print("Moving to Room A.")
  
          grid[1][1] = " "
  
      else:
          print("Room B is clean. Moving to Room A.")
          grid[0][0] = "V"
  
  display_grid()
  print("Both rooms clean. Goal Achieved.\n")

while True:
  print("\n========== MAIN MENU ==========")
  print("1. Tic-Tac-Toe")
  print("2. Vacuum Cleaner")
  print("3. Exit")
  
  choice = input("Enter your choice: ")
  
  if choice == "1":
      tic_tac_toe()
  
  elif choice == "2":
      vacuum_cleaner()
  
  elif choice == "3":
      print("Exiting program.")
      break
  
  else:
      print("Invalid choice. Try again.")
