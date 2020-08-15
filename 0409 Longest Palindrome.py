# https://leetcode.com/problems/longest-palindrome/
# Leetcode August 2020 Week 2 Questions

from collections import Counter

"""Idea: Count up unique letters and calculate
- If even, add to total
- If odd, track that odd exists
- If odd, add -1 of it to total
return total or total + 1 based on odd existing
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        length = 0
        existsOdd = False
        
        for key, val in d.items():
            if val % 2 == 0:
                length += val
            else:
                existsOdd = True
                length += val - 1
        return length if not existsOdd else length + 1
        
