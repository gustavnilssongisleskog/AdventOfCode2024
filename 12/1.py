
grid = []
inp = input()
while inp != "":
    grid.append(inp)
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

vis = [[False] * m for _ in range(n)]

tot = 0

for i in range(n):
    for j in range(m):
        if vis[i][j]:
            continue

        vis[i][j] = True

        plant = grid[i][j]
        perim = 0

        points = set([(i, j)])
        q = [(i, j)]
        for cur in q:
            for dir in dirs:
                next = add(dir, cur)
                if not inside(next):
                    perim += 1
                    continue
                if plant != grid[next[0]][next[1]]:
                    perim += 1
                elif not vis[next[0]][next[1]]:
                    vis[next[0]][next[1]] = True
                    q.append(next)
                    points.add(next)
        tot += perim * len(points)


print(tot)

