N = 4

def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


# Generate neighbors by swapping two rows' queen positions
def get_neighbors(state):
    neighbors = []

    for row1 in range(N):
        for row2 in range(row1 + 1, N):
            neighbor = list(state)

            # Swap queen positions
            neighbor[row1], neighbor[row2] = (
                neighbor[row2], neighbor[row1]
            )

            neighbors.append((tuple(neighbor), row1, row2))

    return neighbors


def print_grid(state):
    print("\nChessboard Grid:")
    for row in range(N):
        for col in range(N):
            if state[row] == col:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


def hill_climbing(initial_state):
    current = tuple(initial_state)

    while True:
        current_cost = cost(current)

        print("\nCurrent state:", current)
        print("Current cost:", current_cost)

        print_grid(current)

        if current_cost == 0:
            print("Goal reached!")
            return current

        neighbors = get_neighbors(current)

        print("\nNeighbor costs:")
        for neighbor, row1, row2 in neighbors:
            print(
                f"Swap rows {row1} and {row2}: "
                f"{neighbor}, cost = {cost(neighbor)}"
            )
            print_grid(neighbor)

        min_cost = min(cost(neighbor) for neighbor, _, _ in neighbors)

        # Stop if no better neighbor exists
        if min_cost >= current_cost:
            print("Local minimum reached; stopping.")
            return current

        # Choose the first neighbor with minimum cost
        best_neighbor, row1, row2 = next(
            (neighbor, r1, r2)
            for neighbor, r1, r2 in neighbors
            if cost(neighbor) == min_cost
        )

        print(f"\nSelected swap: rows {row1} and {row2}")
        current = best_neighbor


initial_state = (3, 1, 2, 0)
solution = hill_climbing(initial_state)

print("\nFinal state:", solution)
print("Final cost:", cost(solution))
print_grid(solution)
