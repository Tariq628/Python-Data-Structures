def insertionSort(arr, length):
    print(arr)
    for i in range(1, length):
        value = arr[i]
        position = i
        while position>0 and arr[position-1] > value:
            arr[position] = arr[position-1]
            position -= 1
        arr[position] = value
    return arr

list = [9, 8, 7, 6, 5]
print(insertionSort(list, len(list)))