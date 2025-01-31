def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive only!"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number must be positive only!"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6)) 

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "The number must be positive only!"
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(n//10)
    
print(sumOfDigits(11))

def power(x,n):
    assert int(n) == n, "Integers Only!"
    if n == 0:
        return 1
    elif n < 0:
        return 1/x * power(x,n+1)
    else:
        return x * power(x,n-1)
    
print(power(2,-4))

def gcd(n,m):
    assert int(n) == n and int(m) == m, "Positive Integers Only"
    if m == 0:
        return n
    return gcd(m, n%m)

print(gcd(48,18))
            
def decimaltobinary(n):
    assert int(n) == n and n >= 0, "Only positive integers"
    if n // 2 == 0:
        return n
    else:
        return str(decimaltobinary(n//2)) + str(n%2)
    
print(decimaltobinary(10))

def decimalToBinary2(n):
    assert int(n) == n and n >= 0, "Only positive integers"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary2(n//2)
    
print(decimalToBinary2(10))

def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:-1])

def flatten(arr):
    result_arr = []
    for i in arr:
        if type(i) is list:
            result_arr.extend(flatten(i))
        else:
            result_arr.append(i)
    return result_arr

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    else:
        result.append(arr[0][0].upper() + arr[0][1:])
        return result + capitalizeFirst(arr[1:])
    
def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2 == 0:
            sum += obj[key]
    return sum

def capitalizeWords(arr):
    result_arr = []
    if len(arr) == 0:
        return result_arr
    result_arr.append(arr[0].upper())
    return result_arr + capitalizeWords(arr[1:])

def stringifyNumbers(obj):
    new_obj = obj
    for i in new_obj:
        if type(new_obj[i]) is int:
            new_obj[i] = str(new_obj[i])
        if type(new_obj[i]) is dict:
            stringifyNumbers(new_obj[i])
    return new_obj


def collectStrings(obj):
    new_arr = []
    for i in obj:
        if type(obj[i]) is str:
            new_arr.append(obj[i])
        if type(obj[i]) is dict:
            new_arr = new_arr + collectStrings(obj[i])
    return new_arr