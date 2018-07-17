def splitter(num):
    
    res =[]
    if num[0] == '0':
        res.append(0)
    num = int(num)
    while num > 0:
        res.append(num % 10)
        num //= 10
    return res[::-1]


def list2str(mas):
    s = ""
    for el in mas:
        s += str(el)
    return s

a = splitter(str(raw_input()))
count_num = [0,0,0]
last_20 = 0
for i in range(len(a)-1):
    count_num[a[i]] += 1
    if(a[i+1] == 0 and count_num[2] > 0):
        
        a[last_20:i+1] = [0]*count_num[0] + [1]*count_num[1] + [2]*count_num[2]
        count_num = [0, 0 , 0]
        last_20 = i + 1
    
count_num[a[-1]] += 1
a[last_20:] = [0]*count_num[0] + [1]*count_num[1] + [2]*count_num[2]
print(list2str(a))