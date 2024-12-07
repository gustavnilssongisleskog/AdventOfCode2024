grid = []
inp = None

while True:
    inp = input()
    if inp == "":
        break

    grid.append(list(inp))

n = len(grid)
m = len(grid[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]



for i in range(n):
    for j in range(m):
        if grid[i][j] == "^":
            cur = (i, j)
            grid[i][j] = "."



def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def inside(pos):
    return 0 <= pos[0] < n and 0 <= pos[1] < m

visited = set()
dir_ind = 0
dir = dirs[0]

while True:
    visited.add(cur)

    next = add(cur, dir)
    while inside(next) and grid[next[0]][next[1]] == "#":
        dir_ind = (dir_ind + 1) % 4
        dir = dirs[dir_ind]
        next = add(cur, dir)
    
    if not inside(next):
        break

    cur = next


print(len(visited))