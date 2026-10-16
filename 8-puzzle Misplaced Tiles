import heapq

def get_misplaced_tiles(state, goal):
    # Count how many tiles are not in their goal position (ignoring the blank tile '0')
    count = 0
    for i in range(len(state)):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_neighbors(state):
    neighbors = []
    # Assume a 3x3 grid (8-puzzle)
    n = 3
    idx = state.index(0)
    row, col = idx // n, idx % n

    # Define possible moves (row_change, col_change)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < n and 0 <= new_col < n:
            new_idx = new_row * n + new_col
            # Create a new state by swapping the blank space
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))

    return neighbors

def a_star(start, goal):
    # Priority queue stores tuples of: (total_estimated_cost, path_cost, current_state, path_taken)
    # f(n) = g(n) + h(n)
    # total_estimated_cost (f) = path_cost (g) + misplaced_tiles (h)
    start_h = get_misplaced_tiles(start, goal)
    queue = [(start_h, 0, start, [start])]

    visited = set()

    while queue:
        f, g, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                neighbor_g = g + 1
                neighbor_h = get_misplaced_tiles(neighbor, goal)
                neighbor_f = neighbor_g + neighbor_h
                heapq.heappush(queue, (neighbor_f, neighbor_g, neighbor, path + [neighbor]))

    return None

# --- Demo / Test ---
# 0 represents the blank space. States are represented as flat tuples of a 3x3 grid.
# 1 2 3
# 4 0 6
# 7 5 8
start_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)
goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)

solution_path = a_star(start_state, goal_state)

if solution_path:
    print(f"Solved in {len(solution_path) - 1} steps!")
    for step, state in enumerate(solution_path):
        print(f"\nStep {step}:")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
else:
    print("No solution found.")
