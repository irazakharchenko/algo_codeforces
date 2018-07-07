n = int(input())

a = []
b = []
for i in range(n):
    a.append(input())


for i in range(n):
    el = input()
    if(el in a):
        a.remove(el)
    else:
        b.append(el)
print(len(a))