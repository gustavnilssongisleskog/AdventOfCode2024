inp = None

grid = []
while True:
    inp = input()
    if inp == "":
        break
    grid.append(list(inp))

moves = []

while True:
    inp = input()
    if inp == "":
        break
    moves += list(inp)


n = len(grid)
m = len(grid[0])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


for i in range(n):
    for j in range(m):
        if grid[i][j] == "@":
            robot = (i, j)

dirs = {
    "v": (1, 0),
    "^": (-1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

for move in moves:
    dir = dirs[move]
    next = add(robot, dir)
    look = next

    while grid[look[0]][look[1]] == "O":
        look = add(look, dir)
    
    if grid[look[0]][look[1]] == "#":
        continue

    grid[look[0]][look[1]] = "O"

    grid[look[0]][look[1]] = "O"
    grid[next[0]][next[1]] = "@"
    grid[robot[0]][robot[1]] = "."

    robot = next


tot = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == "O":
            tot += 100 * i + j

print(tot)