def linearSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return False

print(linearSearch([4,6,7,8,9,1,3,4,5], 5))

import math
def binarySearch(arr, val):
    start = 0
    end = len(arr) - 1
    middle = math.floor((len(arr) - 1)/ 2)
    print(start, middle, end)
    while not arr[middle] == val and start <= end:
        if val < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end)/2)
        print(start, middle, end)
    if arr[middle] == val:
        return middle
    return False
    
print(binarySearch([1,2,3,4,5,6,7,8,9], 7))  