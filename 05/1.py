order = [set() for _ in range(100)]

inp = input()
while inp != "":
    a, b = map(int, inp.split("|"))
    order[a].add(b)
    inp = input()

inp = input()

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
        tot += nums[len(nums) // 2]
    
    
    
    inp = input()


print(tot)