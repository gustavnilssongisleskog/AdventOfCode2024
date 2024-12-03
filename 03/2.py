n = 6

tot = 0
do = True
for _ in range(n):
    s = input()

    for i in range(len(s) - 7):

        if s[i:i + 4] == "do()":
            do = True
        
        if s[i:i + 7] == "don't()":
            do = False

        if not do:
            continue

        if s[i:i + 3] != "mul":
            continue

        if s[i + 3] != "(":
            continue
        
        if not s[i + 4].isdigit():
            continue

        num1_end = i + 4
        while num1_end + 1 < len(s) - 3 and s[num1_end + 1].isdigit():
            num1_end += 1
        
        num1 = int(s[i + 4:num1_end + 1])

        if s[num1_end + 1] != ",":
            continue
        
        if not s[num1_end + 2].isdigit():
            continue

        num2_end = num1_end + 2
        while num2_end + 1 < len(s) - 1 and s[num2_end + 1].isdigit():
            num2_end += 1
        
        num2 = int(s[num1_end + 2:num2_end + 1])

        if s[num2_end + 1] != ")":
            continue

        tot += num1 * num2


print(tot)
        