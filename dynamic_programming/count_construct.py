import sys
from typing import List

def count_construct(query_string: str, substrings: List[str]) -> bool:

    memo = {}
    def helper(query_string, substrings):

        if query_string == '':
            return 1

        if query_string in memo:
            return memo[query_string]

        total_count = 0
        for substr in substrings:
            if query_string.startswith(substr):
                suffix = query_string[len(substr):]
                result = helper(suffix, substrings)
                total_count += result

        memo[query_string] = total_count
        return memo[query_string]
        
    return helper(query_string, substrings)


assert count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) == 2
assert count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) == 1
assert count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']) == 4

print("ok!")
