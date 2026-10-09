import random


grid = [[5, 4, 0], [6, 1, 8], [7, 3, 2]]

goal_state = [[i for i in range(j, j + 3)] for j in range(0, 9, 3)]

def check_goal(grid, goal_state):
    for i in range(3):
        for j in range(3):
            if grid[i][j] != goal_state[i][j]:
                return False
    return True

visited = set()

def get_neighbors(grid):
  neighbors = []

  # Find the blank space (0)
  for i in range(3):
      for j in range(3):
          if grid[i][j] == 0:
              row, col = i, j
              break
      else:
          continue
      break

  # Up, Down, Left, Right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  for dr, dc in directions:
      new_row = row + dr
      new_col = col + dc

      # Check boundaries
      if 0 <= new_row < 3 and 0 <= new_col < 3:
          new_grid = [r[:] for r in grid]

          # Swap blank with adjacent tile
          new_grid[row][col], new_grid[new_row][new_col] = (
              new_grid[new_row][new_col],
              new_grid[row][col]
          )

          neighbors.append(new_grid)

  return neighbors

def dls(grid, goal_state, depth, visited):
    # Check if goal is reached
    if check_goal(grid, goal_state):
        return [grid]

    # Stop if depth limit is reached
    if depth == 0:
        return None

    grid_state = tuple(tuple(row) for row in grid)

    visited.add(grid_state)

    for neighbor in get_neighbors(grid):
        neighbor_state = tuple(tuple(row) for row in neighbor)

        if neighbor_state not in visited:
            result = dls(
                neighbor, goal_state, depth - 1, visited
            )

            if result is not None:
                return [grid] + result

    return None


def ids(grid, goal_state, max_depth=50):
    for depth in range(max_depth + 1):
        visited = set()

        result = dls(grid, goal_state, depth, visited)

        if result is not None:
            print("Goal state found at depth:", depth)
            print("Solution path:")

            for step, state in enumerate(result):
                print(f"\nStep {step}:")
                for row in state:
                    print(row)

            return True

    print("Goal state not found within depth limit.")
    return False

ids(grid, goal_state)
