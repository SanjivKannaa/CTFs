r = [int(i) for i in input().split()][0]
thickness = [int(i) for i in input().split()]
l, w, no_obs = [int(i) for i in input().split()]
obs = []
for i in range(no_obs):
    obs.append([int(i) for i in input().split()])
max_dia = w-2*r #max possible extra thickness (dia)

for i in obs:
    for j in obs:
        if i[0] != j[0] and i[1] != j[1]:
            dist = ((i[0]-j[0])**2 + (i[1]-j[1])**2)**(1/2) - i[2] - j[2]
            if dist < max_dia:
                max_dia = dist

for i in obs:
    if i[1] > w//2:
        dist = w-i[1] - i[2]
        if dist < max_dia:
            max_dia = dist
    else:
        dist = i[1] - i[2]
        if dist < max_dia:
            max_dia = dist

max_dia -= r
#thickness.sort()
count = 0
while(max_dia > 0 and len(thickness) > 0):
    count += 1
    max_dia -= thickness[0]
    thickness.pop(0)
print(count)