
# read four inputs
con1 = input().split(':')
con2 = input().split(':')
con3 = input().split(':')
con4 = input().split(':')

# get bools from pos 1
b1 = con1[1].strip() == 'true'
b2 = con2[1].strip() == 'true'
b3 = con3[1].strip() == 'true'
b4 = con4[1].strip() == 'true'

# count number of true
count = 0
if b1:
    count += 1
if b2:
    count += 1
if b3:
    count += 1
if b4:
    count += 1

if count < 3:
    print('Go fishing!')
else:
    print('Wait for the storm to pass.')