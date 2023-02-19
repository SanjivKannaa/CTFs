a=b=c=d=" "


count = 0
for _ in range(int(input())):
    inp = input()[1:-1]
    if inp[0] == "-" and a!="#":
        count += 1
    if inp[1] == "-" and b!="#":
        count += 1
    if inp[2] == "-" and c!="#":
        count += 1
    if inp[3] == "-" and d!="#":
        count += 1
    a, b, c, d = inp
print(count)