 
n = int(input())

a = [int(x) for x in input().split(" ")]

min_a = min(a)

left = a.count(min_a)
res = n - left
new_min = 1000000
br = False
while left < n and not br and len(a) > 0:
    i = 0
    while i < len(a):
        if a[i] == min_a:
            del(a[i])
        else:
            if a[i] < new_min:
                new_min = a[i]
            i += 1
    if len(a) < left:
        br = True
    min_a = new_min
    new_min = 100000000
    prev = a.count(min_a)
    left -= prev
    if left < 0:
        res += left
        left = 0
    else:
        left += prev
print(res) 
    

        
