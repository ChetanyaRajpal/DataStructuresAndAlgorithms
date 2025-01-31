import numpy as np
def Average_Calculator(arr):
    Total = sum(arr)
    Average = Total / len(arr)
    return Average

# while True:
#     temps = np.array([], dtype=float)
#     n_days = int(input("How many days?"))
#     if n_days < 1:
#         "not valid"
#     n = 1
#     for i in range(n_days):
#         temp = float(input(f"Temp for Day {n} : \n"))
#         temps = np.append(temps,temp)
#         n = n + 1
#         print(temps)
#     print(Average_Calculator(temps))
#     n_days_higher = 0
#     for i in temps:
#         if Average_Calculator(temps) < i:
#             n_days_higher = n_days_higher + 1
#     print(n_days_higher)
    


# temps = list()
# n_days = int(input("How many days: \n"))
# if n_days <= 0 : 
#     print("Invalid")
    
# day = 0
# for i in range(0,n_days):
#     day += 1
#     temp = float(input(f"Temp of day {day} : \n"))
#     temps.append(temp)
#     print(temps)
# average = Average_Calculator(temps)
# print(average)
# n_days_higher = 0
# for i in temps:
#     if i > average:
#         n_days_higher += 1
# print(n_days_higher)
    
        

def two_sums(arr,target_number):
    for i in range(len(arr)):
        if arr[i] + arr[i+1] == target_number:
            return (i,i+1)

print(two_sums([2,7,11,15],9))

def two_sums2(arr,target_number): 
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target_number:
                print(i,j)
            
two_sums2([2,3,8,15,16,7,5,4],9)

def two_sums3(arr,target_number):
    seen = {}
    for i, num in enumerate(arr):
        compliment = target_number - num
        
        if compliment in seen:
            print(seen[compliment], i)
        
        seen[num] = i
        
two_sums3([2,3,8,15,16,7,5,4],9)

def max_product(arr):
    max1 = 0
    max2 = 0 
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i       
        elif i > max2:
            max2 = i
    return max1 * max2

print(max_product([1,2,8,4,6,9]))        

def middle_el(lst):
    return lst[1:-1]

print(middle_el([1,2,3,4]))

def pair_sum(myList, sum):
    new_list = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i] + myList[j] == sum:
                new_list.append(f"{myList[i]}+{myList[j]}")
    return new_list

print(pair_sum([2,4,3,5,6,-2,4,7,8,9],7))

def contains_duplicate(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
        elif i in unique:
            return True
    return False

print(contains_duplicate([1,2,3,4,5]))