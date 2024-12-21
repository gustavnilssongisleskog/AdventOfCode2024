grid = []

inp = input()
while inp != "":
    grid.append([int(x) for x in inp])
    inp = input()

n = len(grid)
m = len(grid[0])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def inside(pos):
    return 0 <= pos[0] < n and 0 <= pos[1] < m

dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def dfs(start):
    def rec(cur):
        num = grid[cur[0]][cur[1]]
        if num == 9:
            return 1
        tot = 0
        for dir in dirs:
            next = add(cur, dir)
            if inside(next) and grid[next[0]][next[1]] == 1 + num:
                tot += rec(next)
        return tot
    return rec(start)

tot = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            tot += dfs((i, j))

print(tot)