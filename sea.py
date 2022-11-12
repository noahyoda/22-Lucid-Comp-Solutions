

l = input()
s = input()

score = 0
ab = 0
sub = 0

i = 0
while i < len(s):
    if s[i] == 'A':
        if i < len(s)-1 and s[i+1] == 'B':
            score += 4
            ab += 1
            i += 1
        else:
            score += 1
    elif s[i] == 'B':
        score += 2
    elif s[i] == 'C':
        sub += 1
    i += 1

score -= sub*(ab**2)

print(score)