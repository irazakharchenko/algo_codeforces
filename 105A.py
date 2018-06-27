#k, l, m, n и d,

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

coun = 0
for i in range(1,d+1):
    if(i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0):
        coun += 1


print(coun)
