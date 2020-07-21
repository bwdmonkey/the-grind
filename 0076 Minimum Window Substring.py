# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        ans, ans_len = "", float("inf")
        l, r, n, m = 0, 0, len(s), len(t)
        
        d = Counter(t)
        # remaining unique token character counts
        remaining = len(d)
        window = defaultdict(lambda: 0)
        
        while r < n:
            # new window, include new character in window count
            c = s[r]
            window[c] += 1
            
            # if token character count matches, dec remaining
            if window[c] == d[c]:
                remaining -= 1
            
            # window contraction
            while l <= r and remaining == 0:
                c = s[l]
                
                if r - l + 1 < ans_len:
                    ans, ans_len = s[l:r + 1], r - l + 1
                
                window[c] -= 1
                if window[c] < d[c]:
                    remaining += 1
                
                l += 1
            r += 1
            
        return ans
