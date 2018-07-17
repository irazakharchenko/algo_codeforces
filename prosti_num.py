li =[]

for i in range(2, 100000+1):
    b = False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            b = True
            break
    if not b:
        li.append(i)

print(li)