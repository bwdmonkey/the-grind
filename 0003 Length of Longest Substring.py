# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Version 1

from collections import OrderedDict

class SolutionOne:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = OrderedDict()
        l = 0
        
        for c in s:
            if c in d:
                if len(d) > l:
                    l = len(d)
                while len(d) > 0 and c != d.popitem(last=False)[0]:
                    pass
            d[c] = True
            
        if len(d) > l:
            l = len(d)
        return l
        
        
# Version 2
class SolutionTwo:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        n = len(s)
        for j in range(n):
            st = set()
            for i in range(j, n):
                if not s[i] in st:
                    st.add(s[i])
                else:
                    break
            result = len(st) if len(st) > result else result
        return result
