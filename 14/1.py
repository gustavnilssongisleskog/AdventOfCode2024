w = 101
h = 103

# w = 11 # 101
# h = 7 # 103

steps = 100

quads = [0,0,0,0]

inp = input()
while inp != "":
    pos, vel = inp.split()
    px, py = pos.split(",")
    px = int(px[2:])
    py = int(py)
    vx, vy = vel.split(",")
    vx = int(vx[2:])
    vy = int(vy)

    x = (px + vx * steps) % w
    y = (py + vy * steps) % h

    if x > w // 2:
        if y > h // 2:
            quads[0] += 1
        elif y < h // 2:
            quads[1] += 1
    elif x < w // 2:
        if y > h // 2:
            quads[2] += 1
        elif y < h // 2:
            quads[3] += 1


    inp = input()


print(quads[0] * quads[1] * quads[2] * quads[3])