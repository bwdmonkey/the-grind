# https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cursum = 0, 0
        d = defaultdict(int)
        # if sum == k, include default 1
        d[0] = 1
        for i in nums:
            cursum += i
            # number of times a subarray with sum k 
            # has occurred up to the current index
            count += d[cursum - k]
            d[cursum] += 1
        return count
            
