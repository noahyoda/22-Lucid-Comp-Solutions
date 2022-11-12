from math import pi as pi
from math import factorial as fact

r, n = input().split()
reef_area = 0
rock = []
rock_area = 0
for i in range(int(n)):
    line = input().split()
    if line[0] == 'reef':
        reef_area += pi * int(line[3]) ** 2
    else:
        rock.append(line[1])
        rock_area += pi * int(line[3]) ** 2

drop_area = pi * int(r) ** 2

p = reef_area / drop_area   # chance of hitting reef
r = rock_area / drop_area   # chance of hitting rock
g = (drop_area - reef_area) / drop_area  # chance of not hitting reef

# chance of winning 1st round = p
# chance of winning 2nd round = (1-p) * r * p
# chance of hitting rock = p * sum((g*r)^i for i in range(1, 3))

#prob = p * sum((g*r)**i for i in range(1, 3))
prob = p /  (1-g*r)

p1 = p
p2 = g*r*p
p3 = g*r*g*r*p

prob = sum([p1, p2, p3])

print(round(prob, 3))