a = [34, 55, 23, 12, 10]
length = len(a)
for i in range(length-1):
    for j in range(length-1-i):
        if a[j] > a[j+1]:
            a[j] , a[j + 1] = a[j + 1], a[j]
print((a))