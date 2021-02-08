def how_sum(target, numbers):

    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        remainder = target - num
        result = how_sum(remainder, numbers)
        if result != None:
            return result + [num]

    return None