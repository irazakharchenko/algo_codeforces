# coins, power
from copy import deepcopy
def killer(bully):
    if(bully == 0):
        return []

    return c[bully - 1][3] + [c[bully -1][0]]



def super_killer(bully):
    if(bully == 0):
        return []

    min_ = min(c[bully - 1][3])

    if(min_ < c[bully -1][0]):
        res = deepcopy(c[bully - 1][3])
        res[res.index(min_)] = c[bully - 1][0]
        return res
    return c[bully - 1][3]

n, k = [int(x) for x in input().split()]

p = [int(x) for x in input().split()]
c = [[int(x)] for x in input().split()]
for i in range(len(c)):
    c[i].append(p[i])
    c[i].append(i)

c.sort(key=lambda x: x[1])

min_nk = min(n,k)

for i in range(min_nk+1):
    c[i].append(killer(i))
for i in range(min_nk+1, n):
    c[i].append(super_killer(i))
c.sort(key=lambda x: x[2])
str_res = ""
for el in c:
    str_res += str(sum(el[3]) + el[0]) + " "

print(str_res[:-1])

