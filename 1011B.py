def put_in_sort( mea, el):
    l = 0
    r = len(mea) - 1
    avg = (l + r) // 2
    print(mea)
    if r == -1:
        return [el]
    while r - l > 1:
        if el == mea[avg]:
            mea = mea[:avg] + [el] + mea[avg:]
            return mea
        elif el < mea[avg]:
            r = avg
        else:
            l = avg
        avg = (l + r) // 2
    if r == l:
        if el > mea[r]:
            if r < len(mea) - 1:
                return mea[:r+1] + [el] + mea[r+1:]
            return mea[:min(r, len(mea))] + [el]

    return mea[:r] + [el] + mea[r:]
        

n, m = [int(x) for x in input().split()]

a =  [int(x) for x in input().split()]

taken = []
meals = []
for i in range(m):
    if a[i] not in taken:
        taken.append(a[i])
        meals.append(a.count(a[i]))
meals.sort(reverse = True)
res = 0
print(meals)
while meals[0] // 2 > meals[-1]:
    diff = meals[0] - meals[0] // 2
    meals = put_in_sort(meals[1:], meals[0] // 2) # get rid of zero elem add it half
    meals = put_in_sort(meals, diff) # add another half
    meals = meals[:min(n, len(meals))] # we don't need meals that are in small quantity
    print(meals)
while n > len(meals):
    diff = meals[0] - meals[0] // 2
    meals = put_in_sort(meals[1:], meals[0] // 2) # get rid of zero elem add it half
    meals = put_in_sort(meals, diff) # add another half
    meals = meals[:min(n, len(meals))] # we don't need meals that are in small quantity
    print(meals)
if n > len(meals):
    res = 0
else:
    res = meals[-1]
print (res)

