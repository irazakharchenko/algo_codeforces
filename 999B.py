from math import floor, sqrt


n = int(input())
s = input()
s = [x for x in s]

div_last_part = []

for i in range(2, int(floor(sqrt(n)))+1):
    if n % i == 0:
        s[:i] = s[i-1::-1]
        div_res = n // i
        if(div_res != i):
            div_last_part.append(div_res)
div_last_part = div_last_part[::-1]
for el in div_last_part:
    s[:el] = s[el-1::-1]
res = ""
s = s[::-1]
for i in range(len(s)):
    res += s[i]
print(res)