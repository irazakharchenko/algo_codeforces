def uniq_num(mas):
    res = 0
    for i in range(len(mas)):
        if mas[i] not in mas[:i]:
            res += 1
    return res

n = int(input())
a = [int(x) for x in input().split()]
taken = []
taken.append(a[0])
res = uniq_num(a[1:])
for i in range(1,n):
    if a[i] not in taken:
        taken.append(a[i])
        res += uniq_num(a[i+1:])

print(res)