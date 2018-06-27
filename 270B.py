n, k = [int(x) for x in input().split()]

f = [int(x) for x in input().split()]

f = sorted(f)
res = 0
num = 0
left = []
while len(f) > 0:
    i = 1
    while i < len(f) and f[i] == f[0]:
        i += 1
    left_in_not0floor = f[i: min(k, len(f))]
    if (k > len(f)):
        res += (f[-1] - 1) * 2
        break

    res += 2 * (f[num] - 1)
    f = f[min(k, len(f)):]
    num = max(k - i -1, 0)

print(res)
