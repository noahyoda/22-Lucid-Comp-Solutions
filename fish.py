

sf, e = input().split()
e = int(e)

events = []
for i in range(e):
    ev, n = input().split()
    events.append((ev, int(n)))

sf = int(sf)
for ev, n in events:
    if ev == 'G':
        sf += n
    else:
        sf -= sf % n

print(sf)