path = input().split()

oxy = int(path[0])

for i in range(1, len(path)):
    oxy -= 1
    if oxy < 0:
        print(0)
        exit()
    if int(path[i]) > oxy:
        oxy = int(path[i])

if oxy >= 0:
    print(1)
    