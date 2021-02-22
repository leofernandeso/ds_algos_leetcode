# https://leetcode.com/problems/count-sorted-vowel-strings/

def count_vowel_strings(n: int) -> int:

    possible_ways_map = dict(zip(['a', 'e','i', 'o', 'u'], [5,4,3,2,1]))
    memo = {}
    def helper(letter, n: int):
        
        if n == 1:
            return 5
        if n == 2:
            memo[letter, n] = sum(
                possible_ways_map[aux_letter] for aux_letter in possible_ways_map if aux_letter >= letter
            )
            return memo[letter, n]

        result = 0
        for l in possible_ways_map:
            if l >= letter:
                result += helper(l, n-1)
        memo[letter, n] = result
        return memo[letter, n]

    return helper('a', n)

print(count_vowel_strings(1))
print(count_vowel_strings(50))

        
        

    
    
