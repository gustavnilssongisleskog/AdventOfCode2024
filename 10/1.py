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


def bfs(start):
    tot = 0
    q = [start]
    vis = set([start])
    for cur in q:
        num = grid[cur[0]][cur[1]]
        for dir in dirs:
            next = add(cur, dir)

            if inside(next) and grid[next[0]][next[1]] == 1 + num and next not in vis:
                vis.add(next)
                q.append(next)
                if num == 8:
                    tot += 1
    
    return tot



tot = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            tot += bfs((i, j))

print(tot)