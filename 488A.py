
n, m = [int(x) for x in input().split()]

x =  [int(x_) for x_ in input().split()]
y =  [int(x_) for x_ in input().split()]

res = ""

for el in x:
    if el in y:
        res += str(el) + " "
print(res[:-1])