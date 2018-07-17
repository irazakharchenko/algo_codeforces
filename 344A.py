n = int(input())
k = 1
prev = input()
for i in range(1,n):
    inp = input()
    if prev != inp:
           k += 1
    prev = inp
print(k)