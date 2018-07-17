from sys import stdout

n = int(input())

l =[1, 1]
r =[n, n]
hist = []
gr = False
it = 0
# 1 x  меньше чем a

# 2 y  меньше чем b

# 3 x  больше чем  a  или y  больше чем b


while True:
    if not gr:
        x = (l[0] + r[0]) // 2
        y = (l[1] + r[1]) // 2
    else:
        x = (l[0] + r[0]) // 2
        y = (l[1] + r[1]) // 2
        it += 1
    print(x, y)
    stdout.flush()
    answ = int(input())
    hist.append((x,y,answ))
    if answ == 0:
        break
    if answ == 1:
        r[0] = x
    elif answ == 2:
        r[1] = y
    else:
        gr = True
        
    
