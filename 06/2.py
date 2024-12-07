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
            start = (i, j)
            grid[i][j] = "."



def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def inside(pos):
    return 0 <= pos[0] < n and 0 <= pos[1] < m


tot = 0

for i in range(n):
    for j in range(m):
        visited = [[0] * m for _ in range(n)]

        if (i, j) == start:
            continue
        
        if grid[i][j] == "#":
            continue

        cur = start
        grid[i][j] = "#"
        dir_ind = 0
        dir = dirs[0]

        while True:
            visited[cur[0]][cur[1]] += 1
            if visited[cur[0]][cur[1]] >= 5:
                tot += 1
                break

            next = add(cur, dir)
            while inside(next) and grid[next[0]][next[1]] == "#":
                dir_ind = (dir_ind + 1) % 4
                dir = dirs[dir_ind]
                next = add(cur, dir)
            
            if not inside(next):
                break

            cur = next
        
        grid[i][j] = "."



print(tot)