n = int(input())

v = []

for i in range(n):
    v.append(list(map(int, input().split())))


tot = 0

for nums in v:
    okAny = False
    for rem in range(len(nums)):
        l = nums[:rem] + nums[rem + 1:]
        inc = l[1] > l[0]
        mul = 1 if inc else -1
        ok = True
        for i in range(1, len(l)):
            if not 1 <= mul * (l[i] - l[i - 1]) <= 3:
                ok = False

        if ok:
            okAny = True
    if okAny:
        tot += 1

print(tot)