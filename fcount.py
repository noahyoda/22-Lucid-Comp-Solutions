line = input()
stock = {'halibut':0, 'mackerel':0, 'salmon':0, 'snapper':0, 'squid':0, 'tuna':0}
exp = ['halibut', 'mackerel', 'salmon', 'snapper', 'squid', 'tuna']

for fish in exp:
    a = list(fish)
    check = all(item in line for item in a)
    if check:
        stock[fish] += 1
        for e in fish:
            line = line.replace(e, '', 1)

for fish in exp:
    print(fish+':'+str(stock[fish]))


# each fish has a unique letter
# count unique letters in line