................4. DFS – Water Jug Problem


def dfs():
    stack = [((0, 0), [])]
    visited = set()

    while stack:
        (a, b), path = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == 0 and b == 1:
            return path

        moves = [
            (2, b),
            (a, 5),
            (0, b),
            (a, 0),
            (a-min(a, 5-b), b+min(a, 5-b)),
            (a+min(b, 2-a), b-min(b, 2-a))
        ]

        for state in moves:
            if state not in visited:
                stack.append((state, path))

    return None

result = dfs()

if result:
    for step in result:
        print(step)
else:
    print("Solution not found")

.....................................5. DFS – Maze Solving


maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

def dfs():
    stack = [(start, [start])]
    visited = set()

    while stack:
        pos, path = stack.pop()

        if pos == goal:
            return path

        if pos in visited:
            continue

        visited.add(pos)
        r, c = pos

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            new = (nr, nc)

            if (0 <= nr < 4 and 0 <= nc < 4
                and maze[nr][nc] == 0
                and new not in visited):

                stack.append((new, path + [new]))

    return None

result = dfs()

if result:
    print("Maze Path:", result)
else:
    print("Path not found")

.....................6. DFS – Blocks World


start = (("A", "B"), ("C",))
goal = (("A",), ("B", "C"))

def clean(state):
    return tuple(sorted(s for s in state if s))

def dfs():
    start_state = clean(start)
    goal_state = clean(goal)

    stack = [(start_state, [start_state])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal_state:
            return path

        if state in visited:
            continue

        visited.add(state)

        for i in range(len(state)):
            block = state[i][-1]
            temp = [list(s) for s in state]
            temp[i].pop()

            for j in range(len(state) + 1):
                if i == j:
                    continue

                new = [s[:] for s in temp]

                if j == len(state):
                    new.append([block])
                else:
                    new[j].append(block)

                nxt = clean(tuple(tuple(s) for s in new))

                if nxt not in visited:
                    stack.append((nxt, path + [nxt]))

    return None

result = dfs()

if result:
    for step in result:
        print(step)
else:
    print("Solution not found")

...................................7. DFS – Missionaries and Cannibals


def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and c > m:
        return False

    if 3-m > 0 and 3-c > 3-m:
        return False

    return True

def dfs():
    stack = [((3, 3, 1), [])]
    visited = set()

    moves = [(1,0), (2,0), (0,1),
             (0,2), (1,1)]

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == (0, 0, 0):
            return path

        m, c, boat = state

        for x, y in moves:
            if boat == 1:
                new = (m-x, c-y, 0)
            else:
                new = (m+x, c+y, 1)

            if valid(new[0], new[1]) and new not in visited:
                stack.append((new, path))

    return None

result = dfs()

if result:
    for step in result:
        print(step)
else:
    print("Solution not found")
