n = int(input())
prev_num = max([int(x) for x in input().split(" ")])
br = False
for i in range(n-1):
    this = [int(x) for x in input().split(" ")]
    if min(this) <= prev_num:
        if max(this) <= prev_num:
            prev_num = max(this)
        else:
            prev_num = min(this)
    else:
        br = True
        break
if br:
    print("NO")
else:
    print("Yes")
