lst = [34, 55, 23, 12, 10, 8, 9]
searchElement = int(input("Enter Digit You Wanna Check: "))
check = ""
index = 0
for i in lst:
    if i is searchElement:
        print(f"Yes Digit Is Prrsent at {index}")
        check = i
        break
    index += 1
if check != searchElement:
    print("Not Prrsent ")