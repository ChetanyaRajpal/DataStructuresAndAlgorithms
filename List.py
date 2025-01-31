integers = [1,2,3,4]
print(integers)

strings = ['one', 'two', 'three']
print(strings)

mix_list = [1,2,'one', 1.2]
print(mix_list)

nested_list = [1,2,3,['name', ' class']]
print(nested_list)

#Accessing/Traversing elements of list

def traverse_list(list):
    for i in list:
        print(i)
    
    for i in range(len(list)):
        list[i] = list[i]+"+"
        print(list[i])
        
traverse_list(strings)

#Update/Insert
integers[2] = 44
print(integers)

#List Methods
#append() - add element at the end of the list
#insert() - add element at the specified position
#extend() - add multiple elements at the end of the List

#remove() - remove the specified element from the list

integers.insert(0,55)
print(integers)

integers.append(99)
new_list = [11,40,50]
integers.extend(new_list)

print(integers)

#Slice/Delete from list

mylist = ['a', 'b', 'c', 'd']
print(mylist[:2] )

mylist[:2] = ['x','y']
print(mylist)

#Pop Method
#pop() - remove the last element from the list and it can also take the index of the element you want to remove.
mylist.pop(0)
print(mylist)

#del method
del mylist[0]
print(mylist)

#Remove method
mylist.remove('c')
print(mylist)

#Searching
new_list = [50,6,7,8,79,41]
target = 50
if target in new_list:
    print("Yes, the element is in there")
else:
    print("Nope")

#Second method
def linear_search_list(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return "Nope"

print(linear_search_list(new_list, 41))

#List Operations/ Functions

a = [1,2,3]
b = [4,5,6]

print(a+b)

print(a * 4)

print(len(new_list))
print(max(new_list))
print(min(new_list))
print(sum(new_list))
print(sum(new_list)/len(new_list))

# total = 0
# count = 0
# while (True):
#     inp = input("Enter a number")
#     if inp == "Done" or inp == "done": break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     average1 = total/count
    
# print(average1)


# Elements_list = []
# while (True):
#     inp = input("Enter a number: \n")
#     if inp == "Done" or inp == "done": break
#     Elements_list.append(float(inp))
#     total = sum(Elements_list)
#     count = len(Elements_list)
#     average = total / count
# print(average)

#Strings and Lists
a = 'spam'
b = list(a)
print(b)

c = "spam-spam-spam"
delimiter = '-'
d = c.split(delimiter)
print(d)

print(delimiter.join(d))

#List Comprehensions
prev_list = [1,2,3,4]
new_list = [i*2 for i in prev_list]
print(new_list)

language = 'Python'
another_list = [item for item in language]
print(another_list)

prev_list = [-1,-1,4,5,6,7]
new_list = [i**2 for i in prev_list if i < 0]
print(new_list)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
numbers_list = list(range(1,21))
print(numbers_list)

fibonacci_series = [fibonacci(i) for i in numbers_list]
print(fibonacci_series)

new_list2 = [n if n > 0 else "Negtive number" for n in prev_list]
print(new_list2)

a = [1,2,3,4]
print(a[3:0:-1])

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))
print(data[0][0])

