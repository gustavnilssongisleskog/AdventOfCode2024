from math import gcd

symbols = [chr(i) for i in range(ord("A"), ord("Z") + 1)] + [chr(i) for i in range(ord("a"), ord("z") + 1)] + [chr(i) for i in range(ord("0"), ord("9") + 1)]

inp = None
grid = []
while True:
    inp = input()
    if inp == "":
        break
    grid.append(inp)


n = len(grid)
m = len(grid[0])

positions = {symbol:[] for symbol in symbols}

for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            continue
        
        positions[grid[i][j]].append((i, j))

def diff(a, b):
    return (a[0] - b[0], a[1] - b[1])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def inside(x):
    return 0 <= x[0] < n and 0 <= x[1] < m

nodes = set()

for symbol in symbols:
    poss = positions[symbol]
    for i in range(len(poss)):
        for j in range(len(poss)):
            if i == j:
                continue
            vec = diff(poss[j], poss[i])
            g = gcd(vec[0], vec[1])
            vec = (vec[0] // g, vec[1] // g)
            node = poss[j]
            while inside(node):
                nodes.add(node)
                node = add(vec, node)

print(len(nodes))