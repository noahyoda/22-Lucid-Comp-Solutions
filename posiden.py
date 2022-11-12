import math

n = int(input())
loc = input().split(',')
loc[0] = loc[0][1:]
loc[-1] = loc[-1][:-1]
walk = []

for i in range(n-2):
    line = input().split()
    dir = line[1]
    dist = int(line[2])
    walk.append((dir, dist))

# find vertical and horizontal distance
v = 0
h = 0
for i in walk:
    if i[0] == 'north':
        v += i[1]
    elif i[0] == 'south':
        v -= i[1]
    elif i[0] == 'east':
        h += i[1]
    elif i[0] == 'west':
        h -= i[1]

# find pace size based on distances
# ie find the greatest common divisor
a = 0 if h == 0 else int(loc[0])/h
b = 0 if v == 0 else int(loc[1])/v

print(int(max(a,b)))