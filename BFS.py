//1. BFS – 8 Puzzle Problem
from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def bfs():
    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()

        if state == goal:
            return path + [state]

        z = state.index(0)
        r, c = divmod(z, 3)

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                new = list(state)
                new[z], new[nz] = new[nz], new[z]
                new = tuple(new)

                if new not in visited:
                    visited.add(new)
                    q.append((new, path + [state]))

    return None

result = bfs()

if result:
    for step in result:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
else:
    print("Solution not found")

...............................2. BFS – Robot Path Planning

from collections import deque

grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

def bfs():
    q = deque([(start, [start])])
    visited = {start}

    while q:
        pos, path = q.popleft()

        if pos == goal:
            return path

        r, c = pos

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            new = (nr, nc)

            if (0 <= nr < 4 and 0 <= nc < 4
                and grid[nr][nc] == 0
                and new not in visited):

                visited.add(new)
                q.append((new, path + [new]))

    return None

result = bfs()

if result:
    print("Robot Path:", result)
else:
    print("Path not found")

..........................3. BFS – Blocks World


from collections import deque

start = (("A", "B"), ("C",))
goal = (("A",), ("B", "C"))

def clean(state):
    return tuple(sorted(s for s in state if s))

def bfs():
    start_state = clean(start)
    goal_state = clean(goal)

    q = deque([(start_state, [start_state])])
    visited = {start_state}

    while q:
        state, path = q.popleft()

        if state == goal_state:
            return path

        for i in range(len(state)):
            block = state[i][-1]
            temp = [list(s) for s in state]
            temp[i].pop()

            for j in range(len(state) + 1):
                new = [s[:] for s in temp]

                if i == j:
                    continue

                if j == len(state):
                    new.append([block])
                else:
                    new[j].append(block)

                nxt = clean(tuple(tuple(s) for s in new))

                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, path + [nxt]))

    return None

result = bfs()

if result:
    for step in result:
        print(step)
else:
    print("Solution not found")
