from collections import defaultdict
nums = list(map(int, input().split()))

num_dict = defaultdict(int)
for num in nums:
    num_dict[num] += 1

for _ in range(25):
    next = defaultdict(int)
    for k, v in num_dict.items():
        if k == 0:
            next[1] += v
        elif len(str(k)) % 2 == 0:
            l = int(str(k)[:len(str(k))//2])
            r = int(str(k)[len(str(k))//2:])
            next[l] += v
            next[r] += v
        else:
            next[2024 * k] += v
    num_dict = next

print(sum(num_dict.values()))