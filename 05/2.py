order = [set() for _ in range(100)]

inp = input()
while inp != "":
    a, b = map(int, inp.split("|"))
    order[a].add(b)
    inp = input()

inp = input()

def compare(x, y):
    if y in order[x]:
        return -1
    if x in order[y]:
        return 1
    return 0

from functools import cmp_to_key

tot = 0
while inp != "":
    nums = list(map(int, inp.split(",")))
    ok = True
    passed = set()
    for num in nums:
        if len(passed.intersection(order[num])) > 0:
            ok = False
            break
        passed.add(num)
    
    if ok:
        inp = input()
        continue
    
    nums = sorted(nums, key=cmp_to_key(compare))
    
    tot += nums[len(nums) // 2]
    inp = input()


print(tot)