
s, n = [int(x) for x in input().split()]


x = []

for i in range(n):
    x.append([int(y) for y in input().split()])

x.sort(key = lambda w: w[0])
br = False
for i in range(n):
    if(s <= x[i][0]):
        br = True
        break
    s += x[i][1]

if br:
    print("NO")
else:
    print("YES")