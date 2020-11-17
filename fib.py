cache = {}

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
    
    return cache[n]

for i in range(11):
    print(f'{i}: {fib(i)}')

    
    