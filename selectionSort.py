a = [34, 55, 23, 12, 10,9,8]
length = len(a)
for i in range(length):
    minidx = i
    for j in range(i+1, len(a)):
        if a[minidx] > a[j]:
            minidx = j
    a[i], a[minidx] = a[minidx], a[i]
    print(a)