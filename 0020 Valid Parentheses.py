# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []        
        bktMap = { ')': '(', '}': '{', ']': '[' }
        
        for c in s:
            if bktMap.get(c, False):
                if not stk or bktMap[c] != stk.pop():
                    return False
            else:
                stk.append(c)
        return len(stk) == 0
                
