from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:        
    
    def helper(l, r):
            
        if r > len(cost) - 1:
            return 0          
        if cost[l] < cost[r]:
            return cost[l] + helper(l, r+1)
        if cost[l] >= cost[r]:
            return min(helper(r, r+1), helper(r, r+2))
    
        
    return helper(0, 1)

assert minCostClimbingStairs([10, 15, 20]) == 15, f"result = {minCostClimbingStairs([10, 15, 20])}"
assert minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6