# https://leetcode.com/problems/group-anagrams/

from collections import Counter, defaultdict

alphabets = "abcdefghijklmnopqrstuvwxyz"

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for word in strs:
            counts = tuple(Counter(alphabets + word).values())
            d[counts].append(word)
        return list(d.values())
