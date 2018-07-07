
def bin_find(ind):
    j = len(x)-1
    max_j = ind

    while j > ind and max_j != j:
        if(x[j] - x[ind] <= d):
            if(max_j < j):
                max_j = j
            j = (j + len(x) - 1) // 2
        else:
            j = (j + ind) // 2
    return j

def fact(num):
    res = 1

    for i in range(2,num+1):
        res *= i
    return res


n, d = [int(x) for x in input().split()]

x = [int(z) for z in input().split()]


res = 0
for i in range(len(x)-2):
    j = bin_find(i)
    if(j - i > 1):
        res += fact(j - i) / fact(2) / fact(j - i - 2)
print(int(res))