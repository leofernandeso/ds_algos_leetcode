# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import deque

def length_of_longest_substring(s: str) -> int:
    char_ix_map = {}
    max_substr_len = 0
    for curr_ix, curr_char in enumerate(s):
        if curr_char in char_ix_map:
            char_ix_map = {
                c: ix for c, ix in char_ix_map.items() if ix > char_ix_map[curr_char]
            }
        char_ix_map[curr_char] = curr_ix
        max_substr_len = max(max_substr_len, len(char_ix_map))
    return max_substr_len

if __name__ == '__main__':
    assert length_of_longest_substring("abcabcbb") == 3, length_of_longest_substring("abcabcbb")
    assert length_of_longest_substring("bbbbb") == 1, length_of_longest_substring("abcabcbb")
    assert length_of_longest_substring("pwwkew") == 3, length_of_longest_substring("pwwkew")
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    