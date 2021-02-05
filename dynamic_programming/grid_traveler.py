import time

def memoized_grid_traveler(m, n):

    memo = {}
    def grid_traveler(m, n, memo):
        if (m, n) in memo:
            return memo[m, n]
        if (n, m) in memo:
            return memo[n, m]
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        result = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
        memo[m, n] = result
        memo[n, m] = memo[m, n]
        return result

    return grid_traveler(m, n, memo)

def grid_traveler(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return grid_traveler(m-1, n) + grid_traveler(m, n-1)

before = time.time()
grid_traveler(15, 15)
print(f"Time elapsed = {time.time() - before} seconds")

before = time.time()
print(memoized_grid_traveler(15, 15))
print(f"Time elapsed = {time.time() - before} seconds")