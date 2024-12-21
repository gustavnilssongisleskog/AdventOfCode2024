inp = None

grid = []
while True:
    inp = input()
    if inp == "":
        break
    grid.append(list(inp.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")))

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

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def mul(a, x):
    return (a[0] * x, a[1] * x)


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

box = list("[]")

for move in moves:
    dir = dirs[move]
    next = add(robot, dir)
    look = next

    if dir[0] == 0:
        # Sideways
        while grid[look[0]][look[1]] in box:
            look = add(add(look, dir), dir)
        
        
        if grid[look[0]][look[1]] == "#":
            continue

        back = sub(look, dir)
        while back != robot:
            grid[look[0]][look[1]] = grid[back[0]][back[1]]
            look = back
            back = sub(back, dir)
        
        grid[look[0]][look[1]] = grid[back[0]][back[1]]
        grid[robot[0]][robot[1]] = "."
        robot = next
        continue


    # Up down

    if grid[look[0]][look[1]] == "#":
        continue


    levels = [set([robot])]

    can_move = True
    for level in levels:
        next_level = set()
        for pos in level:
            look = add(pos, dir)
            if grid[look[0]][look[1]] == "#":
                can_move = False
                break
            
            if grid[look[0]][look[1]] == "[":
                next_level.add(look)
                next_level.add(add(look, (0, 1)))
            if grid[look[0]][look[1]] == "]":
                next_level.add(look)
                next_level.add(add(look, (0, -1)))
        
        if not can_move or len(next_level) == 0:
            break
        levels.append(next_level)
    
    if not can_move:
        continue

    for level in levels[::-1]:
        for pos in level:
            look = add(pos, dir)
            grid[look[0]][look[1]] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = "."
    
    robot = add(robot, dir)

print("\n".join(["".join(grid[i]) for i in range(n)]), end="\n\n\n")

tot = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == "[":
            # tot += 100 * i + min(j, m - j - 1)
            tot += 100 * i + j





print(tot)