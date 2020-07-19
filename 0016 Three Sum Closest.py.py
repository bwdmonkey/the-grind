# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = None
        nums.sort()
        
        for idx, val in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            
            while l < r:
                curr_sum = val + nums[l] + nums[r]
                
                if diff != None:
                    if abs(target - curr_sum) < abs(diff):
                        diff = target - curr_sum
                else:
                    diff = target - curr_sum
                
                if target > curr_sum:
                    l += 1
                else:
                    r -= 1
        
        return target - diff
