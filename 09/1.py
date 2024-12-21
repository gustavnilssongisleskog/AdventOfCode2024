inp = input()

assert len(inp) % 2 == 1

files = []
for i in range(0, len(inp), 2):
    id = i // 2

    for _ in range(int(inp[i])):
        files.append(id)
    
    if i + 1 < len(inp):
        for _ in range(int(inp[i + 1])):
            files.append(-1)

n = len(files)
l = 0
r = n - 1

while r > l:

    while r > l and files[r] == -1:
        r -= 1
    

    while l < r and files[l] != -1:
        l += 1
    
    if l == r:
        break

    files[l] = files[r]
    files[r] = -1

tot = 0
for i in range(n):
    if files[i] == -1:
        break
    tot += i * files[i]

print(tot)