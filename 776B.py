li =[]


n = int(input())
if n > 1:
    li.append(2)
for i in range(2, n+2):
    b = False
    for j in li:
        if i % j == 0:
            b = True
            break
    if not b:
        li.append(i)

res = [ ]
k = 0
is_prosti = False
for i in range(2, n+2):
    if i in li:
        res.append(1)
        is_prosti = True
    else:
        res.append(2)
if not is_prosti:
    print(1)
    res = [1] * n
elif n > 2:
    print(2)
else:
    print(1)
s = ""
for e in res:
    s += str(e) + " "

print(s[:-1])