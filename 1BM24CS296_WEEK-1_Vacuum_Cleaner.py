grid = [[" " for _ in range(2)] for _ in range (2)]

def display_grid():
  for i in range(2):
    for j in range(2):
      print(grid[i][j], end=" | ")
    print("\n--+---+--")

for i in range(2):
  grid[1][i] = "D"

grid[0][0] = "V"

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

print("Both rooms clean. Goal Acheived.\n")
