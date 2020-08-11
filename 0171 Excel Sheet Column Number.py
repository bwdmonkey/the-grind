# https://leetcode.com/problems/excel-sheet-column-number/
# Leetcode August 2020 Challenge Week 2 Questions

# Calculating 1-index char to num
# ord(x) - 64

class Solution:
    def titleToNumber(self, s: str) -> int:
        # Left to Right approach
        # 'ABA' = 26(26(1) + 2) + 1
        res = 0
        for c in s:
            res *= 26
            res += ord(c) - 64
        return res
