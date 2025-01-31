def bubbleSort(custom_arr):
    for i in range(len(custom_arr)-1):
        for j in range(len(custom_arr)-i -1):
            if custom_arr[j] > custom_arr[j+1]:
                custom_arr[j], custom_arr[j+1] = custom_arr[j+1], custom_arr[j]
    print(custom_arr)
    
bubbleSort([5,7,98,9,7,5,4,30])

def selectionSort(custom_arr):
    for i in range(len(custom_arr)):
        min_index = i
        for j in range(i+1, len(custom_arr)):
            if custom_arr[min_index] > custom_arr[j]:
                min_index = j
                
        custom_arr[i], custom_arr[min_index] = custom_arr[min_index], custom_arr[i]
    print(custom_arr)
    
selectionSort([5,7,98,9,7,5,4,30])

def insertionSort(custom_arr):
    for i in range(1, len(custom_arr)):
        key = custom_arr[i]
        j = i - 1
        while j >= 0 and key < custom_arr[j]:
            custom_arr[j + 1] = custom_arr[j]
            j -= 1
        custom_arr[j + 1] = key
    return custom_arr
    
print(insertionSort([5,7,98,9,7,5,4,30]))

import math
def bucketSort(custom_arr):
    number_of_buckets = round(math.sqrt(len(custom_arr)))
    max_num = max(custom_arr)
    arr= []
    
    for i in range(number_of_buckets):
        arr.append([])
        
    for j in custom_arr:
        index = math.ceil(j * number_of_buckets/max_num)
        arr[index-1].append(j)
        
    for i in range(number_of_buckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            custom_arr[k] = arr[i][j]
            k += 1
    return custom_arr

print(bucketSort([5,7,98,9,7,5,4,30]))

def bucketSortNegativeNumbers(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets
 
    buckets = [[] for _ in range(numberofBuckets)]
 
    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)
    
    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = insertionSort(buckets[i])
        sorted_array.extend(buckets[i])
    
    return sorted_array

def merge(custom_list, l, m, r):
    n1 = m -l + 1
    n2 = r - m
    
    left_subarray = n1 * [0]
    right_subarray = n2 * [0]
    
    for i in range(n1):
        left_subarray[i] = custom_list[l + i]
        
    for j in range(n2):
        right_subarray[j] = custom_list[m + j + 1]
        
    i = 0
    j = 0
    k = l
    
    while i < n1 and j < n2:
        if left_subarray[i] <= right_subarray[j]:
            custom_list[k] = left_subarray[i]
            i += 1
        else:
            custom_list[k] = right_subarray[j]
            j += 1
        k += 1
            
    while i < n1:
        custom_list[k] = left_subarray[i]
        i += 1
        k += 1
        
    while j < n2:
        custom_list[k] = right_subarray[j]
        j += 1
        k += 1
        
def mergeSort(custom_list, l, r):
    if l < r:
        m = (l + (r - 1))//2

        mergeSort(custom_list, l, m)
        mergeSort(custom_list, m+1, r)
        merge(custom_list, l,m,r)
    return custom_list

print(mergeSort([5,7,98,9,7,5,4,30], 0, 7))

def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quickSort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quickSort(my_list, left, pivot_index-1)
        quickSort(my_list, pivot_index +1 , right)
    return my_list

my_list = [3,5,0,6,2,1,4]
print(quickSort(my_list, 0, 6))

def heapify(my_list, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and my_list[l] < my_list[smallest]:
        smallest = l
    if r < n and my_list[r] < my_list[smallest]:
        smallest = r
        
    if smallest != i:
        my_list[i], my_list[smallest] = my_list[smallest], my_list[i]
        heapify(my_list, n, smallest)
        
def heapsort(my_list):
    n = len(my_list)
    for i in range(int(n/2)-1, -1 , -1):
        heapify(my_list, n, i)
    for i in range(n-1,0,-1):
        my_list[i], my_list[0] = my_list[0], my_list[i]
        heapify(my_list, i , 0)
    my_list.reverse()

my_list = [3,5,0,6,2,1,4]
heapsort(my_list)
print(my_list)
