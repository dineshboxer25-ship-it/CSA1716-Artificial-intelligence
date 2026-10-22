from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (
        m == 0 or m >= c
    ) and (
        3-m == 0 or 3-m >= 3-c
    )

q = deque([(start, [])])
visited = set()

while q:
    state, path = q.popleft()

    if state in visited:
        continue
    visited.add(state)

    if state == goal:
        for s in path + [state]:
            print(s)
        break

    m, c, boat = state

    for dm, dc in moves:
        if boat == 1:
            nm, nc, nb = m-dm, c-dc, 0
        else:
            nm, nc, nb = m+dm, c+dc, 1

        if valid(nm, nc):
            q.append(((nm, nc, nb), path+[state]))
