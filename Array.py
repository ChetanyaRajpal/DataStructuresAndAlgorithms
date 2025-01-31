#To be able to create arrays we are going to use two modules - Array module and Numpy module.

#Array module
import array
my_array = array.array('i') #We are calling the array module .array and we are then specifying the type of array which in this case is integer ('i').
print(my_array)
my_array1 = array.array('i', [1,2,3,4,5,6]) #Now we are also passing the list of elements as the second argument.
print(my_array1)

#numpy module
import numpy as np
np_array = np.array([], dtype = int)
print(np_array)

np_array1 = np.array([1,2,3,4,5,6])
print(np_array1)

#Insertion to Array
#We are going to do it with array module
my_array1.insert(0,6)
print(my_array1)
my_array1.insert(2,6)
my_array1.insert(8,7)
print(my_array1)

#Array Traversal
def traverse(array):
    for i in array:
        print(i)

traverse(my_array1)

#Accessing an element in an array
def accessElement(array, index):
   if index > len(array) - 1:
       print("Index out of range")
   else:
       print("Here" ,array[index])
       print(len(array))
       
accessElement(my_array1, 8)

#Searching for an Element
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(my_array1, 5))

#Removing an element
my_array1.remove(6)
print(my_array1)

#One Dimensional Array Practice
#Create an array and traverse
#There are two ways we can do that :
test_array = array.array('i', [1,2,3,4,5,6])
print(test_array)

for i in test_array:
    print(i)
    
test_array1 = np.array([1,2,3,4,5,6])
print(test_array1)

for i in test_array1:
    print(i)
    
#Access individual elements through indexes
def access_each_element(array, index):
    if index > len(array) - 1:
        return "Out of order"
    else:
        return array[index]

print(access_each_element(test_array, 6))

#Append any value to the array using append() method
test_array.append(4)
print(test_array)

test_array1 = np.append(test_array1, 7)
print(test_array1)

#Insert value in an array using insert() method
test_array.insert(3,9)
print(test_array)

#Extend python array using extend() method
test_array.extend([12,50,50])
print(test_array)

#Add items frmo list into array using fromlist() method.
list1 = [100,200]
test_array.fromlist(list1)
print(test_array)    

#Remove any array method using remove() method
def remove_element(arr,element):
    if element not in arr:
        return "not in arr"
    else:
        arr.remove(element)
        return arr
    
print(remove_element(test_array,200))

#Remove last array method using pop method
test_array.pop()
print(test_array)

#Fetch any element through its index using index() method.
print(test_array.index(9))

#Reverse a python array using reverse() method
test_array.reverse()
print(test_array)

#Get array buffer information through buffer_info method
print(test_array.buffer_info())

#Check for number of occurences of an element using count() method
print(test_array.count(50))

#Convert array to string using tostring() method
new_array = test_array.tostring()
print(new_array)

#Convert array to a python list with same elements using tolist() method
new_list = test_array.tolist()
print(new_list)

#Append a string to char array using fromstring() method
new_array1 = array.array('i')
new_array1.fromstring(new_array)
print(new_array1)

#Slice elements from an array
print(test_array[:3])

#Two Dimensional Array
two_dimensional_array = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12] , [13,14,15,16]])
print(two_dimensional_array)

#Insertion in 2d array
# new_2d_array = np.insert(two_dimensional_array, 0 , [17,18,19,20], axis=0)
# print(new_2d_array)

new_2d_array = np.append(two_dimensional_array, [[17,18,19,20]], axis=0)
print(new_2d_array)

print(np.shape(new_2d_array))

def access2darray(arr,i,j):
    n_rows = np.shape(arr)[0]
    n_cols = np.shape(arr)[1]
    print(n_rows,n_cols)
    if i > n_rows - 1 or j > n_cols - 1:
        return "Out of index"
    else:
        print(np.shape(arr))
        return arr[i][j]

print(access2darray(new_2d_array,4,4))

#Traversing
def traverse_2d_array(arr):
    n_rows = np.shape(arr)[0] 
    n_cols = np.shape(arr)[1]
    
    for  i in range(n_rows):
        for j in range(n_cols):
            print(arr[i][j])

traverse_2d_array(new_2d_array)

#Searchong
def search_2d_array(arr,search_value):
    n_rows = np.shape(arr)[0]
    n_cols = np.shape(arr)[1]
    
    for i in range(n_rows):
        for j in range(n_cols): 
            if arr[i][j] == search_value:
                return i,j
            
    return "not found"
    
print(search_2d_array(new_2d_array,40))

#Deleting a row or column

second_new_2d_array = np.delete(new_2d_array, 0, axis = 0)
print(second_new_2d_array)

#When to use arrays
#To store multiple variables of same data type
#Random access

#when to avoid
#Different types of datatype
#Reserve Memory
