a, b, x = [int(s) for s in input().split()]
n = a+b
if a >= b:
    s = "0"
    a -= 1
    last_1 = False
else:
    s = "1"
    b -= 1
    last_1 = True
while len(s) < n:
    if x != 0:
        s += "1" if not last_1 else "0"
        last_1 = not last_1
        x -= 1
        if s[-1] == "0":
            a -= 1
        else:
            b -= 1
    
    else:
        if a > 0:
            find_0 = s.find("0")
            s = s[:find_0] + "0" * a + s[find_0:]
            a = 0
        elif s[-1] == "1":
            s += b * "1"
            b = 0
        else:
            find_1 = s.find("1")
            s = s[:find_1] + "1" * b + s[find_1:]
            
print(s)