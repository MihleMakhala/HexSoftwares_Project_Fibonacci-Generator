from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memorized(n):
    if n <=0:
        return "Input must be a positive integer." 
    elif n ==1:
        return 0
    elif n ==2:
        return 1
    return fibonacci_memorized(n-1) + fibonacci_memorized(n-2)

print(fibonacci_memorized(50))
