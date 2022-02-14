check = int(input("Check Digit: "))
a = [2,5,6,7,8,9,2,1]
a.sort()
low = 0
high = len(a)
if high %2 == 0:
    median1 = high//2
    median2 = high//2-1
    median = (median1+median2)//2
else:
    median = high//2
if check is a[median]:
    print("Present")
    exit()
elif check < a[median]:
    high = median - 1
elif check > a[median]:
    low = median + 1
for i in range(low, high):
    if check == a[i]:
        print("Present")
        exit()