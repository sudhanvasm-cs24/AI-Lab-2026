def find_blank(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c
    return None

def get_neighbors(state):
    r, c = find_blank(state)
    neighbors = []

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [row[:] for row in state]
          
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append(new_state)
    return neighbors

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def dfs(current_state, goal_state, visited, path):
    
    state_key = state_to_tuple(current_state)
    
    if current_state == goal_state:
        return True
    
    visited.add(state_key)
    
    neighbors = get_neighbors(current_state)
    
    for neighbor in neighbors:
        neighbor_key = state_to_tuple(neighbor)
        if neighbor_key not in visited:
            path.append(neighbor)
            if dfs(neighbor, goal_state, visited, path):
                return True

            path.pop()
            
    return False

def solve_puzzle(start, goal):
    visited = set()
    path = [start]
    success = dfs(start, goal, visited, path)
    return success, path

initial_state = [[5, 4, 0], [6, 1, 8], [7, 3, 2]]
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

success, path = solve_puzzle(initial_state, goal_state)

print(f"Success: {success}")
if success:
    print("Goal found")
else:
    print("No solution found or state is unreachable.")
