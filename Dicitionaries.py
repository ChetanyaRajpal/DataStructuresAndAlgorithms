#Creating a dictionary
my_dict = dict()
print(my_dict)

my_dict2 = {}
print(my_dict2)

eng_span = dict(one = 'uno', two = 'dos', three = 'tres')
print(eng_span) 

eng_sp2 = {'one' : 'uno', 'two' : 'dos', 'three' : 'tres'}
print(eng_sp2)

list_of_tuples = [('one','uno'),('two','dos'),('three','tres')]
eng_sp3 = dict(list_of_tuples)
print(eng_sp3)

#Updating and inserting new pairs in the dictionary
my_dict3 = {'name' : 'Edy', 'age' : 26}
print(my_dict3)
my_dict3['age'] = 27
my_dict3['name'] = 'Chetanya'
my_dict3['address'] = 'London'
print(my_dict3)

#Traversing through the dictionary
def traverse_dict(dict):
    for key in dict:
        print(key,dict[key])

traverse_dict(my_dict3)

#Searching for a value in dictionary
def search_value(dict, value):
    for i in dict:
        if dict[i] == value:
            return i,value
    return False
    
print(search_value(my_dict3,'Chetanya'))

#Delete an element from Dictionary
del eng_span['one']
removed_element = eng_span.pop('two', None)
print(removed_element)
print(eng_span)

eng_span['five'] = 'five'
print(eng_span)
removed_element = eng_span.popitem()
print(removed_element)
print(eng_span)
eng_span.clear()
print(eng_span)

#Dictionary Methods
my_dict4 = my_dict3.copy()
print(my_dict4)

my_dict5 = {}.fromkeys([1,2,3],0)
print(my_dict5)

print(my_dict4.get('dream','Richest'))

print(my_dict4.items())
print(my_dict4.keys())

print(my_dict4.setdefault('name1', 'added'))
print(my_dict4)

print(my_dict4.values())

my_dict4.update(eng_sp2)
print(my_dict4)

#Dictionary Operations and built in functions
print('three' in my_dict4)
print('tres' not in my_dict4.values())

print(len(my_dict4))
print(all(my_dict4))
print(any(my_dict4))
print(sorted(my_dict4))

#Dictionary Comprehension
import random
city_names = ['Paris', 'Switzerland', 'London', 'New York', 'Norway', 'Amsterdam']
city_temps = {city : random.randint(20,30) for city in city_names}
print(city_temps)

city_temps_greater25 = {city : temps for city,temps in city_temps.items() if temps > 25}
print(city_temps_greater25)

def count_word_frequency(words):
    word_frequency = {}
    for i in words:
        word_frequency[i] = word_frequency.get(i,0) + 1
    return word_frequency
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words)) 

def merge_dicts(dict1, dict2):
    for i in dict2:
        if i not in dict1:
            dict1[i] = dict2[i]
        elif i in dict1:
            dict1[i] += dict2[i]
        
    return dict1
    
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))       

def merge_dicts2(dict1,dic2):
    result = dict1.copy()
    for key,value in dict2.items():
        result[key] = result.get(key,0) + value
        
    return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))

def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}

def filter_dict(my_dict, condition):
    result = {k:v for k,v in my_dict.items() if condition(k,v)}
    return result

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
print(filtered_dict)

def check_same_frequency(list1, list2):
    def counter(lst):
        result = {}
        
        for i in lst:
            result[i] = result.get(i,0) + 1
        return result
    if counter(list1) == counter(list2):
        return True
    return False
    
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))

