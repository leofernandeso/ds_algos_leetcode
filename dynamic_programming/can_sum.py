def can_sum(target, numbers):

    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers):
            return True

    return False

def memoized_can_sum(target, numbers):

    memo = {}
    def can_sum(target):

        # If it is memoized, just return the memoized value
        if target in memo:
            return memo[target]
        if target == 0:
            return True
        if target < 0:
            return False

        for num in numbers:
            remainder = target - num

            if can_sum(remainder):
                memo[remainder] = True
                return True
                
        memo[remainder] = False
        return False

    return can_sum(target)

    
target = 300
arr = [7, 14]

#print(can_sum(target, arr))