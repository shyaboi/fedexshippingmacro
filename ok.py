a = [2,3,4,54]
b = [2,3,5,2]
sa = 0
ab = 0
for i in range(len(a)):
    if a[i] > b[i]:
       sa += 1
    if a[i] < b[i]:
       sb += 1
    else:
        pass
    return [sa,sb]