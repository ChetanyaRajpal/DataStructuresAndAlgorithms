#Creation
new_tuple = 'a','b','c','d'
print(new_tuple)

new_tuple2 = ('a','b','c')
print(new_tuple2)

new_tuple3 = ('a',)
print(new_tuple3)

new_tuple4 = tuple('abcde')
print(new_tuple4)

#Accessing an element of Tuple
print(new_tuple4[2])
print(new_tuple4[::-1])

#Traversing a tuple
for i in new_tuple4:
    print(i)

for i in range(len(new_tuple4)):
    print(new_tuple4[i])
    
#Searching for an element in tuple
def search_tuple(tuple4):
    for i in tuple4:
        if i == 'c':
            return True
    return False

print(search_tuple(new_tuple4))
print('f' in new_tuple)
print(new_tuple.index('a'))

#Tuple Operations/Functions
mytuple1 = (1,2,3,4,5,67)
mytuple2 = (1,2,3,4,5,87)
print(mytuple1*4)

def tuple_element_wise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1,tuple2)))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_element_wise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)


def get_diagonal(tup):
    lst = []
    for i in range(len(tup)):
        lst.append(tup[i][i])
    return tuple(lst)  

input_tuple = (
    (1, 2, 3,5),
    (4, 5, 6,7),
    (7, 8, 9,100),
    (10, 11, 12,13)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)
    
def get_diagonal2(tup):
    return tuple(tup[i][i] for i in range(len(tup)))

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal2(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)

n = int(input())
a = tuple(str(i) for i in range(1,n+1))
b = "".join(a)
print(b)

