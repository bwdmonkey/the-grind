# https://leetcode.com/problems/3sum-smaller

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        
        nums.sort()
        
        for idx, val in enumerate(nums):
            lo, hi = idx + 1, len(nums) - 1
            
            while lo < hi:
                positions = (val, nums[lo], nums[hi],)
                curr_sum = sum(positions)
                
                if curr_sum < target:
                    res += hi - lo
                    lo += 1
                else:
                    hi -= 1
                    
        
        return res
