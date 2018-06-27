from copy import deepcopy

def checker(mas):
    for i in range(len(mas)):
        for j in range(i+1,len(mas)):
            if(not (mas[j] in d[mas[i]])):
                return False
    return True




def add_dict(a, b):
    if (a in d):
        d[a].append(b)
    else:
        d[a] = [b]


n, m = [int(x) for x in input().split()]


d = dict()

for i in range(m):
    a, b = [int(x) for x in input().split()]
    add_dict(a,b)
    add_dict(b,a)


br = False

for key in d:
    if not checker(d[key]):
        print("NO")
        br = True
        break
if(not br):
    print("Yes")














# smat = []
# for i in range(n+1):
#     smat.append(0)
# mat = []
# for i in range(n+1):
#     mat.append(deepcopy(smat))
# for i in range(m):
#     a, b = [ int(x) for x in input().split()]
#     mat[a][b] = 1
#     mat[b][a] = 1
#
# br = False
# for i in range(1,n+1):
#     check = []
#     for j in range(1, n+1):
#         if(mat[i][j] == 1):
#             check.append(j)
#     if(not checker(check)):
#         print("NO")
#         br = True
#         break
# if( not br):
#     print("YES")
#
#
#
