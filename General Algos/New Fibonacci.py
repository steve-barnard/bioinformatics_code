cache = {}

def new_fib(n,k):
    if n in cache:
        return cache[n]
    
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = new_fib(n-1, k) + k * new_fib(n-2, k)
        
    cache[n] = value
    
    return value
    




