n = 140

grid = []
for _ in range(n):
    grid.append(input())

m = len(grid[0])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def inside(x):
    return 0 <= x[0] < n and 0 <= x[1] < m

dirs = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not(i == 0 and j == 0)]

tot = 0

for i in range(n):
    for j in range(m):
        for dir in dirs:
            pos = (i, j)
            s = grid[i][j]
            for _ in range(3):
                pos = add(pos, dir)
                if not inside(pos):
                    break
                s = s + grid[pos[0]][pos[1]]
            
            if s == "XMAS":
                tot += 1

print(tot)
