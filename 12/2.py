
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
group = [[-1] * m for _ in range(n)]
group_points = []
group_sides = []


for i in range(n):
    for j in range(m):
        if vis[i][j]:
            continue
        
        id = len(group_points)
        vis[i][j] = True
        group[i][j] = id

        plant = grid[i][j]

        points = set([(i, j)])
        q = [(i, j)]
        for cur in q:
            for dir in dirs:
                (ii, jj) = add(dir, cur)
                if not inside((ii, jj)):
                    continue
                if plant != grid[ii][jj]:
                    continue
                elif not vis[ii][jj]:
                    vis[ii][jj] = True
                    q.append((ii, jj))
                    points.add((ii, jj))
                    group[ii][jj] = id

        group_points.append(points)
        group_sides.append(0)

# Vertical sides
for col in range(m):
    for dir in [-1, 1]:
        last_neighbor = None if (col + dir == -1 or col + dir == m) else grid[0][col + dir]
        last = grid[0][col]
        id = group[0][col]
        for row in range(1, n):
            if last_neighbor != last:
                if grid[row][col] != last:
                    group_sides[id] += 1
                elif 0 <= col + dir < m and grid[row][col + dir] == last:
                    group_sides[id] += 1
            
            last_neighbor = None if (col + dir == -1 or col + dir == m) else grid[row][col + dir]
            last = grid[row][col]
            id = group[row][col]
        
        if last_neighbor != last:
            group_sides[id] += 1


# Horizontal sides
for row in range(n):
    for dir in [-1, 1]:
        last_neighbor = None if (row + dir == -1 or row + dir == n) else grid[row + dir][0]
        last = grid[row][0]
        id = group[row][0]
        for col in range(1, m):
            if last_neighbor != last:
                if grid[row][col] != last:
                    group_sides[id] += 1
                elif 0 <= row + dir < n and grid[row + dir][col] == last:
                    group_sides[id] += 1
            
            last_neighbor = None if (row + dir == -1 or row + dir == m) else grid[row + dir][col]
            last = grid[row][col]
            id = group[row][col]
        
        if last_neighbor != last:
            group_sides[id] += 1



tot = 0

for i in range(len(group_points)):
    # print(group_sides[i])
    tot += group_sides[i] * len(group_points[i])

print(tot)