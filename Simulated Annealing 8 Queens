
import random
import math

N = 8

# Calculate the number of attacking queen pairs
def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


# Generate a random neighbor by swapping two positions
def random_neighbor(state):
    neighbor = list(state)

    i, j = random.sample(range(N), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

    return tuple(neighbor), i, j

def print_grid(state):
    print("\nChessboard Grid:")
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


def simulated_annealing(initial_state):
    current = tuple(initial_state)
    T = 100.0
    cooling_rate = 0.95
    min_temperature = 0.01
    count = 0

    while T > min_temperature:
        count = count + 1
        print("\nIteration", count)
        current_cost = cost(current)

        print("\nCurrent state:", *current)
        print("Current cost:", current_cost)
        print("Temperature:", round(T, 3))

        if current_cost == 0:
            print("Goal state reached!")
            print("\nIteration", count)
            return current

        next_state, i, j = random_neighbor(current)
        next_cost = cost(next_state)

        # Delta E = current cost - next cost
        delta_E = current_cost - next_cost

        print(f"Swap row {i} and row {j}:",
              *next_state)
        print("Neighbor cost:", next_cost)
        print("Delta E:", delta_E)

        if delta_E > 0:
            # Better state: accept it
            current = next_state
            print("Better state accepted.")

        else:
            # Equal or worse state: probabilistic acceptance
            probability = math.exp(delta_E / T)
            r = random.random()

            print("Acceptance probability:",
            round(probability, 4))
            print("Random number:", round(r, 4))

            if r < probability:
                current = next_state
                print("Neighbor accepted.")
                print_grid(current)
            else:
                continue
                print("Neighbor rejected.")

        # Decrease temperature
        T *= cooling_rate

    print("\nTemperature reached minimum.")
    print("Final state:", *current)
    print("Final cost:", cost(current))

    return current


initial_state = (i for i in range(8))
solution = simulated_annealing(initial_state)

print("\nReturned state:", *solution)
print("Returned cost:", cost(solution))
