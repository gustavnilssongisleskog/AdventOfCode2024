w = 101
h = 103

# w = 11 # 101
# h = 7 # 103


quads = [0,0,0,0]

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def mul(a, x):
    return (a[0] * x, a[1] * x)

def teleport(a):
    return (a[0] % w, a[1] % h)


pos = []
vel = []

inp = input()
while inp != "":
    pos_str, vel_str = inp.split()
    px, py = pos_str.split(",")
    px = int(px[2:])
    py = int(py)
    vx, vy = vel_str.split(",")
    vx = int(vx[2:])
    vy = int(vy)

    pos.append((px, py))
    vel.append((vx, vy))


    inp = input()

n = len(pos)

def display():
    grid = [["." for _ in range(w)] for _ in range(h)]
    for i in range(n):
        grid[pos[i][1]][pos[i][0]] = "#"
    
    print("\n".join(["".join(grid[i]) for i in range(h)]))

def count_connected():
    regions = 0
    vis = [False] * n
    for i in range(n):
        if vis[i]:
            continue
        regions += 1
        vis[i] = True

        q = [i]

        for cur in q:
            for j in range(n):
                if vis[j]:
                    continue
                diff = sub(pos[cur], pos[j])
                if max(diff) <= 1 and min(diff) >= -1:
                    vis[j] = True
                    q.append(j)
    
    return regions

def step(steps):
    for i in range(n):
        pos[i] = add(pos[i], mul(vel[i], steps))
        pos[i] = teleport(pos[i])


# [(139, 6577), (285, 7486), (288, 6880), (290, 6072), (291, 7183), (293, 7890), (294, 5466), (295, 4254), (295, 5264), (295, 8900)]

step(6577)
display()
exit()

counts = []
iter = 8000
step(iter)
while True:

    count = count_connected()
    counts.append((count, iter))

    if count < 100:
        display()

    step(1)

    iter += 1

    if iter % 10000 == 0:
        break

counts.sort()
print(counts[:10])