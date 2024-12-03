a = []
b = []
n = 1000
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

tot = 0
for x in a:
    tot += x * b.count(x)

print(tot)