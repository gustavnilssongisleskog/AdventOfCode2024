import sys
sys.setrecursionlimit(100000)


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
    gx = int(inp[1][2:-1])
    gy = int(inp[2][2:])

    input()

    dp = {}
    def rec(x, y):
        if (x, y) in dp:
            return dp[(x, y)]

        if x < 0 or y < 0:
            return 10**9
        
        if x == 0 and y == 0:
            return 0
        
        val = min(3 + rec(x - ax, y - ay), 1 + rec(x - bx, y - by))
        dp[(x, y)] = val
        return val

    val = rec(gx, gy)
    if val < 10**8:
        tot += val


print(tot)