def triple_step(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)

def memo_triple_step(n, memo):

    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0

    memo[n] = memo_triple_step(n-1, memo) + memo_triple_step(n-2, memo) + memo_triple_step(n-3, memo)
    return memo[n]