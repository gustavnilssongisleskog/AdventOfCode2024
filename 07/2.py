

def possible(target, nums):

    n = len(nums)
    def rec(ind, val):
        if ind == n:
            return val == target

        return rec(ind + 1, val + nums[ind]) or rec(ind + 1, val * nums[ind]) or rec(ind + 1, int(str(val) + str(nums[ind])))

    return rec(1, nums[0])

tot = 0
inp = None
while True:
    inp = input()
    if inp == "":
        break

    inp = inp.split()
    target = int(inp[0][:-1])
    nums = list(map(int, inp[1:]))

    if possible(target, nums):
        tot += target

print(tot)