n, m = [int(x) for x in input().split()]

pa = [int(x) for x in input().split()]
pb = [int(x) for x in input().split()]

end = False

res = []
taken_pair = [[],[]]
for i in range(0, 2*n, 2):
    n_sim = 0
    for j in range(0, 2*m, 2):
        if (pa[i] in pb[j:j + 2]) ^ (pa[i+1] in pb[j:j + 2]):
            if(pb[j:j + 2] in taken_pair[0]):
                tkp = taken_pair[1][taken_pair[0].index(pb[j:j + 2])]
                if ((pa[i] in pb[j:j + 2] and pa[i] == tkp) or pa[i+1] == tkp):
                    n_sim = 2
                    break
            n_sim += 1
            if (pa[i] in pb[j:j + 2]):
                res.append(pa[i])
                taken_pair[1].append(pa[i])
            else:
                res.append(pa[i+1])
                taken_pair[1].append(pa[i+1])
            if(pb[j:j + 2] not in taken_pair[0]):
                taken_pair[0].append(pb[j:j + 2])
    if n_sim > 1:
        end = True
        break

if(end):
    print(-1)
else:
    num_sim = res.count(res[0])
    # if len(res) == 1:
    #     print(1)
    # else:
    #     print(0)
    if num_sim == len(res):
        print(res[0])
    else:
        print(0)