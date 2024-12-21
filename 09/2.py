inp = input()

assert len(inp) % 2 == 1

files = []
for i in range(0, len(inp), 2):
    id = i // 2
    
    if i + 1 < len(inp):
        files.append((id, int(inp[i]), int(inp[i + 1])))
    else:
        files.append((id, int(inp[i]), 0))


n = len(files)
id_move = n - 1
ind = n - 1

while id_move >= 0:

    while files[ind][0] != id_move:
        ind -= 1

    moved = False


    for i in range(ind):
        if files[i][0] == id_move:
            break

        if files[i][2] >= files[ind][1]:
            if i == ind - 1:
                files[ind] = (id_move, files[ind][1], files[ind][2] + files[i][2])
                files[i] = (files[i][0], files[i][1], 0)
                moved = True
                break

            ins = (id_move, files[ind][1], files[i][2] - files[ind][1])
            files[ind - 1] = (files[ind - 1][0], files[ind - 1][1], files[ind - 1][2] + files[ind][1] + files[ind][2])
            files[i] = (files[i][0], files[i][1], 0)
            files.pop(ind)
            files.insert(i + 1, ins)
            moved = True
            break

    id_move -= 1


l = []
for (id, length, free) in files:
    for _ in range(length):
        l.append(id)
    for _ in range(free):
        l.append(0)



tot = 0
for i in range(len(l)):
    tot += i * l[i]

print(tot)