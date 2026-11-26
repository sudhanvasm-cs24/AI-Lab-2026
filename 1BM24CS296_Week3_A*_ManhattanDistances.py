import heapq

def get_manhattan_distance(state, goal):
    # Calculate the sum of Manhattan distances of all tiles from their goal positions
    distance = 0
    n = 3
    for i in range(len(state)):
        val = state[i]
        if val != 0:  # Skip the blank space
            # Current coordinates
            curr_row, curr_col = i // n, i % n
            # Goal coordinates
            goal_idx = goal.index(val)
            goal_row, goal_col = goal_idx // n, goal_idx % n

            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

def get_neighbors(state):
    neighbors = []
    n = 3
    idx = state.index(0)
    row, col = idx // n, idx % n

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < n and 0 <= new_col < n:
            new_idx = new_row * n + new_col
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))

    return neighbors

def a_star_manhattan(start, goal):
    start_h = get_manhattan_distance(start, goal)
    # Queue items: (f_score, g_score, current_state, path_taken)
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
                neighbor_h = get_manhattan_distance(neighbor, goal)
                neighbor_f = neighbor_g + neighbor_h
                heapq.heappush(queue, (neighbor_f, neighbor_g, neighbor, path + [neighbor]))

    return None

# --- Demo / Test ---
start_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)
goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)

solution_path = a_star_manhattan(start_state, goal_state)

if solution_path:
    print(f"Solved in {len(solution_path) - 1} steps using Manhattan Distance!\n")
    for step, state in enumerate(solution_path):
        g = step  # Path cost to reach this state
        h = get_manhattan_distance(state, goal_state)  # Heuristic value
        f = g + h  # Total estimated cost

        print(f"Step {step}: f(n) = {f} (g(n) = {g}, h(n) = {h})")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print("-" * 30)
else:
    print("No solution found.")
