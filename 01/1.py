a = []
b = []
n = 1000
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

a.sort()
b.sort()

tot = 0
for i in range(n):
    tot += abs(a[i] - b[i])


print(tot)