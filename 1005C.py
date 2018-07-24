pow2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]

n = int(input())

mas = [int(i) for i in input().split(" ")]
mas.sort()
res = 0
taken = [False] * n
for i in range(n):
    if i != 0 and mas[i-1] == mas[i]:
        taken[i] = taken[i-1]
        
        continue
    if not taken[i]:
        for el in pow2:
            diff = el - mas[i]
            if diff <= 0 :
                continue
            if diff in mas:
                if diff == mas[i] :
                    if i < n-1 and mas[i] == mas[i+1] : 
                        taken[i] = True
                        taken[mas.index(diff)] = True
                    else:
                        continue
                else:
                    taken[i] = True
                    taken[mas.index(diff)] = True
                
res = taken.count(False)

print(res)