import sys
from typing import List

def can_construct(query_string: str, substrings: List[str]) -> bool:
    
    memo = {}
    def helper(query_string, substrings):

        if query_string in memo:
            return memo[query_string]
            
        if query_string == '':
            return True

        for substr in substrings:
            if query_string.startswith(substr):
                suffix = query_string[len(substr):]
                result = helper(suffix, substrings)
                memo[suffix] = result
                if memo[suffix] == True:
                    memo[query_string] = True
                    return memo[query_string]

        memo[query_string] = False
        return memo[query_string]

    return helper(query_string, substrings)