n,  k = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]


i =0
while i < len(a):
    if(a[i] > k):
        break

    i += 1

count = i
j = len(a) - 1
while j >= i:
    if (a[j] > k):
        break
    count += 1

    j -= 1

print(count)