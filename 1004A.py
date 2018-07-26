n, d = [int(x) for x in input().split()]
x = [int(w) for w in input().split()]
x.sort()
res = 1
for i in range(n):
    if i != 0 and x[i] - x[i-1] >= 2 * d:
        if x[i] - x[i-1] == 2 * d:
            res += 1
        else:
            res += 2
res += 1
print(res)