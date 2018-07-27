n , k = [int(x) for x in input().split()]
MAXV = 999999999999999999999
s = input()
s = list(set(s))
n = len(s)
s.sort()
res = MAXV
cur = 0
st = 0
fin = st + 1
cur = ord(s[st]) - ord("a") + 1
taken = [s[st]]
while len(taken) < k and fin < n:
    
    if ord(s[fin]) - ord(taken[-1]) > 1:
        cur += ord(s[fin]) - ord("a") + 1
        taken.append(s[fin])
    fin += 1

if len(taken) == k:
    print(cur)
else:
    print(-1)