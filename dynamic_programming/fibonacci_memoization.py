import functools

def recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

# python provides function call kwargs memorization
@functools.lru_cache
def functools_mem_fib(n):
    if n <= 2:
        return 1
    else:
        return functools_mem_fib(n-1) + functools_mem_fib(n-2)

# manual memoization -- caching function call results
def mem_fib(n):
    memo = {}
    def fib(n, memo):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]
    return fib(n, memo)

recursive_fib(20)
functools_mem_fib(20)
mem_fib(20)