n = int(input())
a = [int(x) for x in input().split(" ")]
res = 0
l = [a[0], 0]
r = [a[-1], n -1]
while l[1] < r[1]:
    if l[0] == r[0]:
        res = l[0]
    elif l[0] < r[0]:
        l[1] += 1
        l[0] += a[l[1]]
        continue
    r[1] -= 1
    r[0] += a[r[1]]
print(res)
        
