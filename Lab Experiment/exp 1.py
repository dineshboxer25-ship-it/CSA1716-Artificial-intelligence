import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_pos = tile - 1
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)
    return distance

def solve(start):
    pq = [(manhattan(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal:
            print("Solved in", len(path) - 1, "moves\n")
            for step, s in enumerate(path):
                print("Step", step)
                for i in range(0, 9, 3):
                    print(" ".join("_" if x == 0 else str(x)
                                   for x in s[i:i+3]))
                print()
            return

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = row + dr, col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                pos = r * 3 + c
                new_state = list(state)
                new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
                new_state = tuple(new_state)

                if new_state not in visited:
                    heapq.heappush(pq, (
                        g + 1 + manhattan(new_state),
                        g + 1,
                        new_state,
                        path
                    ))

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
solve(start)
