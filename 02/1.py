n = int(input())

v = []

for i in range(n):
    v.append(list(map(int, input().split())))


tot = 0

for nums in v:
    inc = nums[1] > nums[0]
    mul = 1 if inc else -1
    ok = True
    for i in range(1, len(nums)):
        if not 1 <= mul * (nums[i] - nums[i - 1]) <= 3:
            ok = False

    if ok:
        tot += 1

print(tot)