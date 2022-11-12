n, q = input().split()
sizes = [int(i) for i in input().split()]
#ans = []
for i in range(int(q)):
    query = input().split()
    start = int(query[0]) - 1
    end = int(query[1])
    x = sizes[start]
    for j in range(start+1, end):
        x = x ^ sizes[j]
    #ans.append(x)
    print(x)
