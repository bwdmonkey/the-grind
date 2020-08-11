# https://leetcode.com/problems/h-index/
# Leetcode August 2020 Week 2 Questions

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for idx, cites in enumerate(citations):
            if cites >= n - idx:
                return n - idx
        return 0
