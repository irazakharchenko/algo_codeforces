n = int(input())

a = [int(x) for x in input().split()]

res = 0
d = set(a)
res = max([a.count(x) for x in d])
print(res)