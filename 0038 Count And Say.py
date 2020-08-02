# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'
        
        prev = self.countAndSay(n - 1)
        res, prev_c, count = '', prev[0], 0
        
        for c in prev:
            if prev_c != c:
                res += str(count) + prev_c
                prev_c, count = c, 1
            else:
                count += 1
        
        res += str(count) + prev_c
        return res
