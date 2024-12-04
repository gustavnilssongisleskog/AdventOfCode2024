n = 140

grid = []
for _ in range(n):
    grid.append(input())

m = len(grid[0])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, x):
    return (a[0] * x, a[1] * x)

def inside(x):
    return 0 <= x[0] < n and 0 <= x[1] < m

dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

tot = 0

for i in range(1, n - 1):
    for j in range(1, m - 1):
        num_mas = 0
        for dir in dirs:
            s = ""
            pos = add((i, j), mul(dir, -1))
            s = grid[pos[0]][pos[1]]

            for _ in range(2):
                pos = add(pos, dir)
                s = s + grid[pos[0]][pos[1]]
            
            if s == "MAS":
                num_mas += 1
        
        if num_mas == 2:
            tot += 1

print(tot)
