r = [int(i) for i in input().split()][0]
thickness = [int(i) for i in input().split()]
l, w, no_obs = [int(i) for i in input().split()]
obs = []
for i in range(no_obs):
    obs.append([int(i) for i in input().split()])
max_dia = w-2*r #max possible extra thickness (dia)

for i in obs:
    if i[1] >= w/2:
        dist = w - i[1] - i[2]
        if dist < max_dia:
            max_dia = dist
    else:
        dist = i[1] - i[2]
        if dist < max_dia:
            max_dia = dist
    for j in obs:
        if i[0] != j[0] or i[1] != j[1]:
            dist = ((i[0]-j[0])**2 + (i[1]-j[1])**2)**(1/2) - i[2] - j[2]
            if dist < max_dia:
                max_dia = dist


thickness.sort()
count = 0
max_inc = max_dia/2 - r
temp = 0

for i in thickness:
    temp += i
    count += 1
    if temp >= max_inc:
        break




if count != 0:
    print(count)
else:
    print(-1)