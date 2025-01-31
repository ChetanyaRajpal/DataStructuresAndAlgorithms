

# 0 1 1 2 3 5 8 13 21
def check_is_fibo (n):
    a = 0
    b = 1
    c = 1
    if(n == a or n == b):
        return True
    while(c<n):
        c = a + b
        a = b
        b = c
        if (c == n):
            return True
    return False

print(check_is_fibo(4181))
