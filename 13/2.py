

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

tot = 0



while True:
    inp = input().split()
    if len(inp) == 0:
        break
    ax = int(inp[2][2:-1])
    ay = int(inp[3][2:])
    inp = input().split()
    bx = int(inp[2][2:-1])
    by = int(inp[3][2:])

    inp = input().split()
    gx = int(inp[1][2:-1]) + 10000000000000
    gy = int(inp[2][2:]) + 10000000000000

    inp = input()

    det = ax * by - ay * bx
    print(det)
    if det != 0:
        a = by * gx - bx * gy
        b = -ay * gx + ax * gy
        if a % det != 0:
            continue
        if b % det != 0:
            continue

        a = a // det
        b = b // det

        if a < 0 or b < 0:
            continue
        
        tot += 3 * a + b
        continue

    print("K")
    

print(tot)