from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    result = []
    for i in range(len(nums) // 2):
        result.append(nums[i])
        result.append(nums[i+n])
    return result

assert shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7]
assert shuffle([1,2,3,4,4,3,2,1], 4) == [1,4,2,3,3,2,4,1]
